import requests
from config import SEEDR_EMAIL, SEEDR_PASSWORD

BASE_URL = "https://www.seedr.cc/rest"

session = requests.Session()


def login():
    r = session.post(
        f"{BASE_URL}/login",
        data={"username": SEEDR_EMAIL, "password": SEEDR_PASSWORD},
        timeout=30
    )
    r.raise_for_status()


def add_torrent(link: str):
    login()

    r = session.post(
        f"{BASE_URL}/torrent/add",
        data={"torrent_magnet": link},
        timeout=30
    )
    r.raise_for_status()

    return r.json()
