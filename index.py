import requests
import random
import string
import time

def gerar_link_discord():
    # Escolhe aleatoriamente entre os dois formatos de link
    formato_link = random.choice([
        "https://promos.discord.gg/",
        "https://discord.com/billing/promotions/"
    ])

    # Gera a sequência alfanumérica aleatória
    caracteres = string.ascii_letters + string.digits
    sequencia_aleatoria = ''.join(random.choice(caracteres) for i in range(23))

    # Constrói o link completo
    link_completo = formato_link + sequencia_aleatoria

    return link_completo

def tentar_validar_link(link):
  # URL da API do Discord para promoções (especulativa)
  api_url = "https://discord.com/api/v9/promotions"  

  # Dados da requisição (especulativos)
  payload = {
      "code": link.split("/")[-1],  # Extrai o código do link
      "context": {
          "location": "billing",  # Informação extraída do código HTML
          "referrer": "https://discord.com/billing/promotions"  # Informação extraída do código HTML
      }
  }

  headers = {
      "Content-Type": "application/json",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
  }

  try:
      response = requests.post(api_url, json=payload, headers=headers)
      response.raise_for_status()  # Lança uma exceção para erros HTTP
      print(f"Resposta da API: {response.status_code} - {response.text}")
      return response.json()  # Retorna os dados da resposta em formato JSON

  except requests.exceptions.RequestException as e:
      print(f"Erro na requisição: {e}")
      return None

while True:
    link_gerado = gerar_link_discord()
    print(f"Link gerado: {link_gerado}")

    # Tenta validar o link usando a API
    resposta_api = tentar_validar_link(link_gerado)
    if resposta_api:
        # Analise a resposta da API para determinar se o link é válido
        # ...
        pass

    # Aguarda 1 milissegundo
    time.sleep(0.001)
