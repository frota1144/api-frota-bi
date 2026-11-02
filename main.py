import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

ANULA_API_URL = "https://api.anulamultas.com.br/v1/multas"
HEADERS = {
    "Authorization": "Bearer am_live_cdef0f0646b6_7a0b45344ce70d1879a9bc09583dc1a6",
    "Accept": "application/json"
}

@app.get("/")
def root():
    return {"mensagem": "API do Power BI está ativa!"}

@app.get("/api/v1/bi/multas")
def obter_multas_bi():
    try:
        resposta = requests.get(ANULA_API_URL, headers=HEADERS, timeout=30)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro na Anula Multas: {str(e)}")

@app.get("/api/v1/bi/condutores")
def obter_condutores_bi():
    url_condutores = "https://api.anulamultas.com.br/v1/condutores"
    try:
        resposta = requests.get(url_condutores, headers=HEADERS, timeout=30)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro na Anula Multas: {str(e)}")
