#codigo_12
#import codigo_12

#print(codigo_12.saudacao("Michael"))

#celsius_for_fahrenheit
#from codigo_15 import celsius_for_fahrenheit

#c1 = celsius_for_fahrenheit(25)

#print(f'Resultado celsius_for_fahrenheit {c1}')

def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.2
    return imposto

preco_produto1 = input('Digite o valor do produto 01: ')
preco_produto2 = input('Digite o valor do produto 02: ')

imposto_produto1 = calcular_imposto(int(preco_produto1))
imposto_produto2 = calcular_imposto(int(preco_produto2))

print(imposto_produto1)
print(imposto_produto2)

