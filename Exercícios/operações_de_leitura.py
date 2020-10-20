from os import chdir, getcwd #importa a dunção chdir
chdir('dados') #muda para o diretório dados
print('O diretório atual é:', getcwd())
arquivo = open('Planetas-Sequencial', 'r') #abre o arquivo para leitura
conteudo = arquivo.read()
print('O conteudo completo do arquivo é: \n' + conteudo)
arquivo.close() #fechar arquivo
arquivo = open ('Planetas-Sequencial', 'r') #abre novamente o arquivo
conteudo_parcial = arquivo.read(8) #lê 8 caracteres do arquivo
print('Os 8 primeiros caracteres do arquivo são: \n' + conteudo_parcial) #imprime o que acaba de ser lido
conteudo_parcial = arquivo.read(3) #ler mais 3 caracteres do conteudo
print('Os próximos 3 caracteres do arquivo são: \n' + conteudo_parcial) #imprime o que acaba de ser lido
arquivo.close() #fecha o arquivo