import random

def gerar_senha(tamanho):
    caracteres = 'abcdef12345%$#'
    senha = "".join(random.sample(caracteres, tamanho))
    return senha

print(gerar_senha(10))