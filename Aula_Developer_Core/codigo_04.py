word         = "ovo"
palavra_aux  = ""
palavra_aux1 = ""

for palavra in reversed(word):
    palavra_aux = palavra_aux + palavra

for palavra in (word):
    palavra_aux1 = palavra_aux1 + palavra

print(palavra_aux); 
print(palavra_aux1); 

if (palavra_aux == palavra_aux1):
    print("É Palíndromo")   
else :
    print("Não é Palíndromo")
     



