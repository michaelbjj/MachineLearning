#Trabalhando com arquivos
#arquivo = open(r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt", 'r')

#conteudo = arquivo.read()

#print(conteudo)

#arquivo.close()

#with open(r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt", 'r') as arquivo:
#    conteudo = arquivo.read()
#    print(conteudo)

with open(r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt", 'r') as arquivo :
    print(arquivo.read())    
    arquivo.seek(0)
    print(arquivo.readline())
    arquivo.seek(0)
    print(arquivo.readlines())