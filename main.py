@app.get("/api/v1/bi/multas")
def obter_multas_bi():
    url_alvo = f"{BASE_URL}/multas" # Ajuste o caminho da Anula Multas conforme a documentação deles
    try:
        resposta = requests.get(url_alvo, headers=HEADERS, timeout=30)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro na integração: {str(e)}")
