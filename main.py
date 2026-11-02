import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="API Frota - Integração Power BI")

# Rota de teste para verificar se a API está a funcionar
@app.get("/")
def inicio():
    return {"mensagem": "API do Power BI está ativa!"}

# Rota principal para o Power BI consumir os dados
@app.get("/api/v1/bi/multas")
def obter_dados_bi():
    # Estrutura base pronta para integrar com a URL do Anula Multas
    dados_exemplo = [
        {
            "id_multa": 1,
            "ait": "A012345678",
            "placa": "ABC-1234",
            "status": "Indicação Pendente",
            "valor": 195.23
        }
    ]
    return dados_exemplo
