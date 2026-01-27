import requests

# URL fictícia por enquanto (mock)
DOWNLOAD_API_URL = "https://example.com/api/add"

def aria2_add(link: str):
    """
    Envia o link para uma API externa de download.
    Por enquanto é um mock compatível com Railway.
    """

    # validações básicas
    if not link.startswith(("magnet:", "http://", "https://")):
        return {"error": "Link inválido"}

    # ⚠️ MOCK (simula sucesso)
    return {
        "result": "ok",
        "message": "Download enviado para a fila"
    }

    # 🔜 quando criarmos a API real, será algo assim:
    # response = requests.post(
    #     DOWNLOAD_API_URL,
    #     json={"link": link},
    #     timeout=10
    # )
    # return response.json()
