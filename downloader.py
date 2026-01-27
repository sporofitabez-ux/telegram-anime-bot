import requests
import json
import os

ARIA2_RPC = os.getenv("ARIA2_RPC", "http://localhost:6800/jsonrpc")

def aria2_add(link: str):
    payload = {
        "jsonrpc": "2.0",
        "id": "qwer",
        "method": "aria2.addUri",
        "params": [[link]]
    }

    r = requests.post(ARIA2_RPC, data=json.dumps(payload))
    return r.json()
