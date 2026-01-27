import os
import requests
import json
from config import DOWNLOAD_DIR, ARIA2_RPC_URL, ARIA2_SECRET

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def aria2_add(uri):
    payload = {
        "jsonrpc": "2.0",
        "id": "qwer",
        "method": "aria2.addUri",
        "params": [
            f"token:{ARIA2_SECRET}" if ARIA2_SECRET else [],
            [uri],
            {
                "dir": DOWNLOAD_DIR
            }
        ]
    }

    response = requests.post(ARIA2_RPC_URL, json=payload)
    return response.json()
