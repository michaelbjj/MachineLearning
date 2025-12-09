import requests

#Requisição GET

resposta = requests.get("https://api.github.com")
print(resposta.status_code)
print(resposta.json())

dados = {"nome" : "Michael", "idade" : 44}
resposta = requests.post("https://exemplo.com/api", json=dados)
print(resposta.status_code)