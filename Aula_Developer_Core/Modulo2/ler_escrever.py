#Trabalhando com arquivos
#arquivo = open(r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt", 'r')

#conteudo = arquivo.read()

#print(conteudo)

#arquivo.close()

#with open(r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt", 'r') as arquivo:
#    conteudo = arquivo.read()
#    print(conteudo)

#with open(r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt", 'r') as arquivo :
#    print(arquivo.read())    
#    arquivo.seek(0)
#    print(arquivo.readline())
#    arquivo.seek(0)
#    print(arquivo.readlines())

#sArquivo = r'C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt'

#with open (sArquivo, 'w') as arquivo:
#    arquivo.write("Primeira Linha\n")
#    arquivo.writelines(["Segunda linha\n", "Terceira linha\n"])

#import csv

#with open("dados.csv", "w", newline="") as arquivo:
#    escritor = csv.writer(arquivo)
#    escritor.writerow(["Nome", "Idade", "Cidade"])
#    escritor.writerow(["Michael", 43, "Curitiba"])

#with open("dados.csv", "r") as arquivo :
#    leitor = csv.reader(arquivo)
#    for linha in leitor:
#        print(linha)

#try:
#    with open('arquivo_insexistente.txt', "r") as arquivo:
#        conteudo = arquivo.read()
#except FileExistsError:
#    print("Arquivo não encontrado!")
#except Exception as e:
#    print(f"Ocorreu um erro:{e}")

#import os

#os.rename(r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt", "novo_nome.txt")

#os.remove("novo_nome.txt")

#Exemplos
#origemt  = "C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\origem.txt"
#destinot = "C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\destino.txt"

#with open(origemt, "r") as origem, open(destinot, "w") as destino:
#    destino.write(origem.read())

# import csv

# estoquet = r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\estoque.csv"

# dados = [
#     {"Produtos":"Teclado", "Quantidade": 10, "Preço":100},
#     {"Produtos":"Monitor", "Quantidade": 15, "Preço":150}
# ]

# with open(estoquet, "w", newline="") as arquivo :
#     escritor = csv.DictWriter(arquivo, fieldnames=["Produtos", "Quantidade", "Preço"])
#     escritor.writeheader()
#     escritor.writerows(dados)

textot = r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\texto.txt"

with open(textot, "r") as arquivo :
    palavra = arquivo.read().split()
    print(f"Número de palavras:{len(palavra)}")