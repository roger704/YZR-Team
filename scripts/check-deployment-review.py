#!/usr/bin/env python3
"""Fail-closed client for Nexus's deployment-review decision contract (server required)."""
import argparse
import http.client
import json
import os
import re
import urllib.error
import urllib.request
import urllib.parse

ENDPOINT = 'https://agent.sicken.work/nexus/api/projects/deployment-preflight'
SHA = re.compile(r'[0-9a-f]{40}\Z')
REPO = re.compile(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z')


class Denied(ValueError):
    pass


def verify(value, repository, target, required):
    if not isinstance(value, dict) or value.get('contract_version') != 'nexus-deployment-review.v1':
        raise Denied('invalid_contract')
    if value.get('repository') != repository or value.get('target_sha') != target or value.get('decision') != 'allow':
        raise Denied('deployment_not_authorized')
    pr = value.get('pull_request', {})
    review = value.get('review', {})
    if not isinstance(pr, dict) or not isinstance(review, dict):
        raise Denied('invalid_evidence')
    if pr.get('merged') is not True or pr.get('merge_commit_sha') != target or pr.get('repository') != repository or not isinstance(pr.get('number'), int) or isinstance(pr.get('number'), bool) or pr['number'] <= 0:
        raise Denied('unbound_merge_commit')
    head = pr.get('head_sha')
    if not isinstance(head, str) or not SHA.fullmatch(head) or review.get('head_sha') != head or review.get('status') != 'complete' or review.get('coverage_complete') is not True or type(review.get('unresolved_blockers')) is not int or review.get('unresolved_blockers') != 0 or not review.get('workflow_id'):
        raise Denied('review_incomplete')
    # The fixed Nexus server verifies producer identity and immutable refs.
    # A merge SHA may differ from the PR head only when the server has verified
    # identical Git trees and a first parent bound to the reviewed target base.
    # This client does not independently grant trust to an arbitrary head check.
    checks = value.get('checks')
    if not isinstance(checks, list):
        raise Denied('checks_missing')
    for context in required:
        matches = [c for c in checks if isinstance(c, dict) and c.get('context') == context]
        if len(matches) != 1 or matches[0].get('conclusion') != 'success' or matches[0].get('sha') not in (head, target) or matches[0].get('trusted_producer') is not True:
            raise Denied('required_check_unsatisfied')
    return {'allowed': True, 'repository': repository, 'target_sha': target, 'pull_request': pr['number'], 'reviewed_head': head, 'workflow_id': review['workflow_id']}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise Denied('redirect_refused')


def github_oidc_token():
    url = urllib.parse.urlsplit(os.environ.get('ACTIONS_ID_TOKEN_REQUEST_URL', ''))
    hostname = url.hostname or ''
    # GitHub's runner supplies this URL from its trusted SystemConnection, and
    # GitHub documents requesting the token from that URL (not one fixed host):
    # https://docs.github.com/en/actions/reference/security/oidc#methods-for-requesting-the-oidc-token
    # The anchored suffix is GitHub's DNS zone, not user-owned github.io hosting.
    # TLS verifies that host; lookalikes, userinfo, other ports and redirects fail.
    # Code that can replace the runner environment can already read its token;
    # this client must run only in the trusted deployment job, never PR tests.
    if url.scheme != 'https' or not hostname.endswith('.actions.githubusercontent.com') or url.username or url.password or url.port not in (None, 443) or url.fragment:
        raise Denied('oidc_request_url_invalid')
    request_token = os.environ.get('ACTIONS_ID_TOKEN_REQUEST_TOKEN')
    if not request_token:
        raise Denied('oidc_request_credential_missing')
    query = [(key, value) for key, value in urllib.parse.parse_qsl(url.query, keep_blank_values=True) if key != 'audience']
    query.append(('audience', ENDPOINT))
    destination = urllib.parse.urlunsplit((url.scheme, url.netloc, url.path, urllib.parse.urlencode(query), ''))
    req = urllib.request.Request(destination, headers={'Authorization': 'Bearer ' + request_token})
    with urllib.request.build_opener(NoRedirect).open(req, timeout=30) as response:
        raw = response.read(65537)
        if len(raw) > 65536:
            raise Denied('oidc_response_too_large')
        value = json.loads(raw)
        token = value.get('value') if isinstance(value, dict) else None
        if not isinstance(token, str) or len(token) > 16384 or not re.fullmatch(r'[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+', token):
            raise Denied('oidc_response_invalid')
        return token


def request(repository, target, required, token, oidc=False):
    body = json.dumps({'repository': repository, 'target_sha': target, 'required_checks': required}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, headers={'Content-Type': 'application/json', **({'Authorization': 'Bearer ' + token} if oidc else {'x-api-token': token})}, method='POST')
    with urllib.request.build_opener(NoRedirect).open(req, timeout=30) as response:
        raw = response.read(65537)
        if len(raw) > 65536:
            raise Denied('response_too_large')
        return json.loads(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--github-oidc', action='store_true', help='Use ephemeral GitHub Actions OIDC for this read-only preflight')
    parser.add_argument('--repository', required=True)
    parser.add_argument('--sha', required=True, help='Exact commit that will be deployed')
    parser.add_argument('--require-check', action='append', required=True)
    args = parser.parse_args()
    args.repository = args.repository.lower()
    try:
        if not REPO.fullmatch(args.repository) or not SHA.fullmatch(args.sha) or any(not c or len(c) > 128 for c in args.require_check) or len(set(args.require_check)) != len(args.require_check):
            raise Denied('invalid_request')
        token = github_oidc_token() if args.github_oidc else os.environ.get('NEXUS_DEPLOYMENT_PREFLIGHT_TOKEN')
        if not token:
            raise Denied('preflight_credential_missing')
        decision = verify(request(args.repository, args.sha, args.require_check, token, args.github_oidc), args.repository, args.sha, args.require_check)
        print(json.dumps(decision))
        return 0
    except (ValueError, OSError, urllib.error.URLError, http.client.HTTPException):
        # Do not relay server error bodies, credentials or exception messages.
        print(json.dumps({'allowed': False, 'error': 'deployment_review_preflight_failed'}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
