import requests
from fastapi import APIRouter, HTTPException, status

router = APIRouter()

BASE_URL = "https://api.anulamultas.com.br/v1"  # Exemplo
HEADERS = {"Authorization": "Bearer SEU_TOKEN"}

@router.get("/api/v1/bi/multas")
def obter_multas_bi():
    url_alvo = f"{BASE_URL}/multas"
    
    try:
        resposta = requests.get(url_alvo, headers=HEADERS, timeout=30)
        resposta.raise_for_status()
        return resposta.json()
        
    except requests.exceptions.HTTPError as err_http:
        # Repassa o código de status exato retornado pela API de destino (ex: 401, 404, 403)
        status_code = err_http.response.status_code if err_http.response is not None else status.HTTP_500_INTERNAL_SERVER_ERROR
        detalhe = err_http.response.text if err_http.response is not None else str(err_http)
        raise HTTPException(status_code=status_code, detail=f"Erro na API externa: {detalhe}")
        
    except requests.exceptions.RequestException as err_req:
        # Trata erros de conexão, timeout ou DNS
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Falha na comunicação com a API externa: {str(err_req)}"
        )
