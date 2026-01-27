import aria2p
import os

DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret=""
    )
)

def download(url):
    download = aria2.add_uris([url], options={"dir": DOWNLOAD_DIR})
    download.wait_for_complete()
    return download.files[0].path
