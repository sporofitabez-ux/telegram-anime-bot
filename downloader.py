import aria2p
import os

aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret=""
    )
)

def download_link(link):
    if link.startswith("magnet:"):
        download = aria2.add_magnet(link)
        return download
    else:
        download = aria2.add_uris([link])
        return download
