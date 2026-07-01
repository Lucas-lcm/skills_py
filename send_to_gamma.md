# Skill: send_to_gamma

## Descrição
Esta skill executa um script Python via Shell local para enviar arquivos Markdown estruturados diretamente para a API do Gamma App, gerando apresentações de slides prontas.

## Requisitos de Execução
O script requer 4 argumentos posicionais obrigatórios via linha de comando:
1. `title` (String): Título da aula/apresentação.
2. `file_path` (String): Caminho local do arquivo `.md` gerado.
3. `numCards` (Integer): Quantidade total de slides estimada.
4. `api_key` (String): Chave secreta da API do Gamma App.

## Assinatura do Comando no Shell
```bash
python send_to_gamma.py "<title>" "<file_path>" <numCards> "<api_key>"
```

## Diretrizes para o Agente

    Use esta ferramenta sempre que finalizar a geração e gravação local de uma aula em Markdown destinada a virar slides.

    Garanta que todas as aspas duplas de argumentos com espaços (como o título) estejam devidamente escapadas ou envolvidas se necessário no comando Shell.
---

### 2. `send_to_gamma.py` (Script Python)

```python
# ---
# name: send_to_gamma
# version: 1.0.0
# entry_point: main
# ---

import sys
import json
import requests

def main():
    if len(sys.argv) < 5:
        print("Erro: Argumentos insuficientes.")
        print("Uso: python send_to_gamma.py '<title>' '<file_path>' <numCards> '<api_key>'")
        sys.exit(1)

    title = sys.argv[1]
    file_path = sys.argv[2]
    
    # Tratamento crucial: sys.argv captura tudo como string. 
    # A API do Gamma exige um tipo Number inteiro no JSON para o 'numCards'.
    try:
        numCards = int(sys.argv[3])
    except ValueError:
        print("Erro: O argumento numCards deve ser um número inteiro válido.")
        sys.exit(1)
        
    api_key = sys.argv[4]

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
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    
    payload = {
        "textMode": "generate",
        "format": "presentation",
        "numCards": numCards,  # Enviado como inteiro puro
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
```
