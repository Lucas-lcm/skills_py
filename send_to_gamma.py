# ---
# name: send_to_gamma
# version: 1.0.0
# entry_point: main
# ---

import sys
import json
import requests

def main():
    title = sys.argv[1]
    file_path = sys.argv[2]
    numCards = sys.argv[3]

    # 1. Ler o conteúdo em Markdown do arquivo local
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except Exception as e:
        print(f"Erro ao ler arquivo local: {e}")
        sys.exit(1)

    # 2. Configurar o Payload exato que a API do Gamma exige
    url = "https://public-api.gamma.app/v1.0/generations"
    headers = {
        "X-API-KEY": "sk-gamma-QzEpXndZCNwqZVBxFfEXdRkyMt7uCReWOZi7ZMvok", # COLOQUE SUA CHAVE REAL AQUI
        "Content-Type": "application/json"
    }
    
    payload = {
        "textMode": "generate",
        "format": "presentation",
        "numCards": numCards,
        "title": title,
        "inputText": markdown_content
    }

    # 3. Disparar a requisição
    print(f"Enviando '{title}' para o Gamma App...")
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code in [200, 201]:
        print("Sucesso! Payload aceito pelo Gamma.")
        print(response.text)
    else:
        print(f"Erro {response.status_code}: {response.text}")

if __name__ == "__main__":
    main()