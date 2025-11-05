#frutas = ['maça', 'banana', 'laranja']
#print(frutas)
#print(frutas[0])
#print(type(frutas))

#lista = ["carro",  True, 2, 3.5]
#print(lista)
#print(lista[2])
#print(type(lista[2]))

#Tupla

#tupla = ("carro", True, 2, 3.5)
#print(tupla)
#print(type(tupla))
#print(tupla[3])

#dicionario = {"nome": "Asaph", "logica" : True, "numero": 2, "outro_numero": 3.5}

#print(dicionario)
#print(type(dicionario))
#print(dicionario["logica"])

pessoa = {"nome": "Asaph", "idade": 20, "cidade": "Curitiba"}
print(pessoa["cidade"])

print(pessoa.keys())

print(pessoa.values())

print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")