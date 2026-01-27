import aria2p
from config import DOWNLOAD_DIR

client = aria2p.Client(
    host="http://localhost",
    port=6800,
    secret=""
)

aria2 = aria2p.API(client)

def baixar(link):
    return aria2.add_uris([link], options={"dir": DOWNLOAD_DIR})
