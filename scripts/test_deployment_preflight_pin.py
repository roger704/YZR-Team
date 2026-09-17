"""Execute the actual workflow gate locally without an OIDC credential/network call."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CLIENT = ROOT / 'scripts/check-deployment-review.py'
WORKFLOW = (ROOT / '.github/workflows/deploy.yml').read_text()
STEPS = WORKFLOW.split('      - name: Require reviewed deployment source\n')[1:]
assert STEPS, 'Required deployment gate is absent'
COMMANDS = []
for step in STEPS:
    section = step.split('\n      - ', 1)[0]
    body = section.split('        run: |\n', 1)[1]
    COMMANDS.append('\n'.join(line[10:] for line in body.splitlines() if line.startswith('          ')))
assert all(command == COMMANDS[0] for command in COMMANDS), 'Deployment gates differ'
COMMAND = COMMANDS[0]


@unittest.skipUnless(sys.platform.startswith("linux"), "Production pin checks require Linux sha256sum")
class WorkflowPinTests(unittest.TestCase):
    def run_gate(self, alteration=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'scripts').mkdir()
            target = root / 'scripts/check-deployment-review.py'
            target.write_bytes(CLIENT.read_bytes())
            if alteration == 'modified':
                target.write_text(target.read_text() + '\nprint("UNTRUSTED_CLIENT_EXECUTED")\n')
            elif alteration == 'directory':
                target.unlink()
                target.mkdir()
            elif alteration == 'symlink':
                target.rename(root / 'real-client.py')
                target.symlink_to(root / 'real-client.py')
            # A repository-controlled stdlib name must not execute under python -I.
            (root / 'scripts/json.py').write_text('raise RuntimeError("UNTRUSTED_IMPORT_EXECUTED")\n')
            env = {key: value for key, value in os.environ.items() if key in ('PATH', 'SYSTEMROOT')}
            env.update(DEPLOY_REPOSITORY='roger704/example', DEPLOY_SHA='a' * 40,
                       PYTHONPATH=str(root / 'scripts'))
            return subprocess.run(['bash', '-c', COMMAND], cwd=root, env=env,
                                  capture_output=True, text=True, timeout=15)

    def test_exact_client_runs_isolated_and_fails_closed_without_identity(self):
        result = self.run_gate()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout), {'allowed': False, 'error': 'deployment_review_preflight_failed'})
        self.assertNotIn('UNTRUSTED_IMPORT_EXECUTED', result.stderr)

    def test_modified_client_stops_before_python(self):
        result = self.run_gate('modified')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')

    def test_nonregular_client_stops_before_checksum(self):
        result = self.run_gate('directory')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')
        self.assertEqual(result.stderr, '')

    def test_symlink_client_stops_before_python(self):
        result = self.run_gate('symlink')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, '')


if __name__ == '__main__':
    unittest.main()
