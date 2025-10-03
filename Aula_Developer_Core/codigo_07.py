#numero_01 = int(input('Digite o primeiro numero :'))
#numero_02 = int(input('Digite o segundo numero :'))

#soma = numero_01 + numero_02
#substracao = numero_01 - numero_02

#print(f'A soma dos seus número é: {soma}')
#print(f'A substração dos seus número é: {substracao}')

#valor = float(input('Digite o valor da sua compra :'))

#if valor > 100:
#    desconto = valor * 0.1
#    print(f'Você ganhou R$ {desconto: .2f} de desconto')
#else:
#    print(f'Você não ganhou desconto menor que 100')

#frutas = {'Abacaxi', 'Manga', 'Banana', 'Laranja'}

#for fruta in frutas:
#    print(f'Eu gosto de {frutas}')
  

nome  = str(input('Qual é o seu nome ?'))  
idade = int(input('Qual é a sua idade :'))  
count = 1

if idade >=18:
    print(f'Você user pode acessar o sistema {nome}, pois ja tem {idade} anos')
else :
    print(f'WhatFuck {nome}, você só tem {idade} anos')

while count <= idade:
    print(f'{count}')
    count +=1 
    



