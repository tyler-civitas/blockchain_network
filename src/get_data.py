import requests
from requests.auth import HTTPBasicAuth
import json


def node_rpc(
          rpc_id="test",
          cmd="getblockchaininfo",
          verbose=False,
          url='http://localhost:2000',
          params=None):

    credfile = "/Users/tyler/.aws/bitnodecreds"
    with open(credfile) as f:
        user = f.readline().strip()
        pw = f.readline().strip()
    auth = HTTPBasicAuth(user, pw)

    heads = {
        'Content-Type': 'text/plain',
            }

    data = {
        "jsonrpc": 1,
        "id": rpc_id,
        "method": cmd,
        "params": params
           }

    r = requests.post(
        url=url,
        headers=heads,
        data=json.dumps(data),
        auth=auth
                     )

    if verbose == True:
        print_response_attrs(r)

    return r.json()


def print_response_attrs(r):
        print "\n"
        print "-" * 50
        print "RESPONSE"
        print "-" * 50
        attrs = [
           'apparent_encoding', 'elapsed', 'encoding',
           'ok', 'reason', 'status_code', 'url'
               ]
        for item in attrs:
            print "{:20} : {}".format(item, getattr(r, item))

        print "\n"
        print "-" * 50
        print "HEADERS"
        print "-" * 50
        for i, v in r.headers.items():
            print "{:20} : {:40}".format(i, v)
        print "\n"


if __name__ == "__main__":
    node_rpc(verbose=True)



#
# POST  HTTP/1.1
# Host: localhost:2000
# Content-Type: text/plain
# Authorization: Basic dWJ1bnR1OmNsdXN0ZXJfMQ==
# Cache-Control: no-cache
# Postman-Token: ba54ff40-8610-a8b1-84fd-d43604f9eace
#
# {
# "jsonrpc": 1,
# "id": "test",
# "method": "getblockchaininfo"
# }
