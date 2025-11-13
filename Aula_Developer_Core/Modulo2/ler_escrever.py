#Trabalhando com arquivos
arquivo = open(r"C:\Projetos\Projetos ItValley\Aula_Developer_Core\Modulo2\exemplo.txt", 'r')

conteudo = arquivo.read()

print(conteudo)

arquivo.close()