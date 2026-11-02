import requests
from fastapi import FastAPI, HTTPException, Query
from typing import Optional

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

# --- ROTA PARA O POWER BI CONSUMIR MULTAS ---
@app.get("/api/v1/bi/multas")
def obter_multas_bi(
    placa: Optional[str] = Query(None, description="Filtrar por placa do veículo"),
    status: Optional[str] = Query(None, description="Filtrar por status da multa"),
    data_de: Optional[str] = Query(None, alias="data_ocorrencia_de", description="YYYY-MM-DD"),
    data_ate: Optional[str] = Query(None, alias="data_ocorrencia_ate", description="YYYY-MM-DD"),
    limite: int = Query(100, ge=1, le=100, description="Máximo de registros por página (Max 100)"),
    pagina: int = Query(1, ge=1, description="Número da página")
):
    url_alvo = f"{BASE_URL}/multas"
    
    parametros = {
        "limite": limite,
        "pagina": pagina
    }
    
    if placa:
        parametros["placa"] = placa
    if status:
        parametros["status"] = status
    if data_de:
        parametros["data_ocorrencia_de"] = data_de
    if data_ate:
        parametros["data_ocorrencia_ate"] = data_ate

    try:
        resposta = requests.get(url_alvo, headers=HEADERS, params=parametros, timeout=15)
        resposta.raise_for_status()
        return resposta.json()

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro na integração com Anula Multas: {str(e)}"
        )

# --- ROTA PARA CONSUMIR CONDUTORES ---
@app.get("/api/v1/bi/condutores")
def obter_condutores_bi(
    cpf: Optional[str] = Query(None, description="Filtrar por CPF do condutor"),
    nome: Optional[str] = Query(None, description="Filtrar por nome do condutor")
):
    url_alvo = f"{BASE_URL}/condutores"
    parametros = {}
    
    if cpf:
        parametros["cpf"] = cpf
    if nome:
        parametros["nome"] = nome

    try:
        resposta = requests.get(url_alvo, headers=HEADERS, params=parametros, timeout=15)
        resposta.raise_for_status()
        return resposta.json()
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao buscar condutores: {str(e)}"
        )
