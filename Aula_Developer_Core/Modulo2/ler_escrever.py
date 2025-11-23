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

import csv

with open("dados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade", "Cidade"])
    escritor.writerow(["Michael", 43, "Curitiba"])

with open("dados.csv", "r") as arquivo :
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)