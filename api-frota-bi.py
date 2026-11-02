import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="API Frota - Integração Power BI")

# --- CONFIGURAÇÕES DA API DO ANULA MULTAS ---
BASE_URL = "https://portal-api.anulamulta.com.br/public/v1"
API_TOKEN = "am_live_cdef0f0646b6_7a0b45344ce70d1879a9bc09583dc1a6"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json"
}

@app.get("/")
def inicio():
    return {"mensagem": "API do Power BI está ativa!"}

@app.get("/api/v1/bi/multas")
def obter_dados_bi():
    try:
        resposta = requests.get(f"{BASE_URL}/multas", headers=HEADERS, timeout=30)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro na Anula Multas: {str(e)}")

@app.get("/api/v1/bi/condutores")
def obter_condutores_bi():
    try:
        resposta = requests.get(f"{BASE_URL}/condutores", headers=HEADERS, timeout=30)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro na Anula Multas: {str(e)}")
