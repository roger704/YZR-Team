import copy
import importlib.util
import pathlib
import unittest
import json
import os
from unittest.mock import patch, MagicMock

spec=importlib.util.spec_from_file_location('gate',pathlib.Path(__file__).with_name('check-deployment-review.py'))
gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)
HEAD='a'*40;TARGET='b'*40

def valid():
 return {'contract_version':'nexus-deployment-review.v1','repository':'owner/repo','target_sha':TARGET,'decision':'allow','pull_request':{'repository':'owner/repo','number':1,'merged':True,'head_sha':HEAD,'merge_commit_sha':TARGET},'review':{'workflow_id':'workflow1','head_sha':HEAD,'status':'complete','coverage_complete':True,'unresolved_blockers':0},'checks':[{'context':'documentation','conclusion':'success','sha':HEAD,'trusted_producer':True},{'context':'test','conclusion':'success','sha':TARGET,'trusted_producer':True}]}

class GateTests(unittest.TestCase):
 def check(self,v): return gate.verify(v,'owner/repo',TARGET,['documentation','test'])
 def test_merge_commit_can_differ_from_reviewed_head(self): self.assertTrue(self.check(valid())['allowed'])
 def test_failclosed_cases(self):
  cases=[('decision','pending'),('target_sha',HEAD),('contract_version','v0'),('pull_request',{}),('review',{}),('checks',[])]
  for key,value in cases:
   with self.subTest(key=key):
    v=valid();v[key]=value
    with self.assertRaises(gate.Denied):self.check(v)
 def test_review_and_merge_binding(self):
  for section,key,value in [('pull_request','merged',False),('pull_request','merge_commit_sha',HEAD),('pull_request','repository','other/repo'),('review','head_sha',TARGET),('review','coverage_complete',False),('review','unresolved_blockers',1),('review','status','pending')]:
   with self.subTest(key=key):
    v=valid();v[section][key]=value
    with self.assertRaises(gate.Denied):self.check(v)
 def test_ci_identity_failures(self):
  for key,value in [('sha','c'*40),('conclusion','skipped'),('trusted_producer',False)]:
   v=valid();v['checks'][0][key]=value
   with self.assertRaises(gate.Denied):self.check(v)
  v=valid();v['checks'].append(copy.deepcopy(v['checks'][0]))
  with self.assertRaises(gate.Denied):self.check(v)
 def test_redirect_does_not_forward_auth(self):
  with self.assertRaises(gate.Denied):gate.NoRedirect().redirect_request(None,None,None,None,None,None)

class OidcClientTests(unittest.TestCase):
 def test_untrusted_oidc_urls_fail_before_network(self):
  for url in ['http://pipelines.actions.githubusercontent.com/token','https://evil.invalid/token','https://evilactions.githubusercontent.com/token','https://actions.githubusercontent.com/token','https://pipelines.actions.githubusercontent.com.evil.invalid/token','https://user:pass@pipelines.actions.githubusercontent.com/token','https://pipelines.actions.githubusercontent.com:444/token']:
   with patch.dict(os.environ,{'ACTIONS_ID_TOKEN_REQUEST_URL':url,'ACTIONS_ID_TOKEN_REQUEST_TOKEN':'secret'}), patch.object(gate.urllib.request,'build_opener') as opener:
    with self.assertRaises(gate.Denied):gate.github_oidc_token()
    opener.assert_not_called()
 def test_ephemeral_fetch_fixed_audience_and_no_secret_in_url(self):
  response=MagicMock();response.__enter__.return_value=response;response.read.return_value=json.dumps({'value':'aaa.bbb.ccc'}).encode()
  opener=MagicMock();opener.open.return_value=response
  with patch.dict(os.environ,{'ACTIONS_ID_TOKEN_REQUEST_URL':'https://pipelines.actions.githubusercontent.com/token?api-version=1&audience=other','ACTIONS_ID_TOKEN_REQUEST_TOKEN':'secret-sentinel'}),patch.object(gate.urllib.request,'build_opener',return_value=opener):
   self.assertEqual(gate.github_oidc_token(),'aaa.bbb.ccc')
   req=opener.open.call_args.args[0]
   self.assertNotIn('secret-sentinel',req.full_url)
   self.assertEqual(gate.urllib.parse.parse_qs(gate.urllib.parse.urlsplit(req.full_url).query)['audience'],[gate.ENDPOINT])
   self.assertEqual(req.get_header('Authorization'),'Bearer secret-sentinel')
 def test_github_owned_regional_host_is_not_a_lookalike(self):
  response=MagicMock();response.__enter__.return_value=response;response.read.return_value=b'{"value":"aaa.bbb.ccc"}'
  opener=MagicMock();opener.open.return_value=response
  with patch.dict(os.environ,{'ACTIONS_ID_TOKEN_REQUEST_URL':'https://region.pipelines.actions.githubusercontent.com/token','ACTIONS_ID_TOKEN_REQUEST_TOKEN':'synthetic-token'}),patch.object(gate.urllib.request,'build_opener',return_value=opener):
   self.assertEqual(gate.github_oidc_token(),'aaa.bbb.ccc')
   self.assertEqual(gate.urllib.parse.urlsplit(opener.open.call_args.args[0].full_url).hostname,'region.pipelines.actions.githubusercontent.com')
 def test_oidc_preflight_does_not_mix_operator_header(self):
  response=MagicMock();response.__enter__.return_value=response;response.read.return_value=b'{}'
  opener=MagicMock();opener.open.return_value=response
  with patch.object(gate.urllib.request,'build_opener',return_value=opener):
   gate.request('owner/repo',TARGET,['documentation'],'ephemeral',True)
   req=opener.open.call_args.args[0]
   self.assertEqual(req.get_header('Authorization'),'Bearer ephemeral')
   self.assertIsNone(req.get_header('X-api-token'))

if __name__=='__main__':unittest.main()
