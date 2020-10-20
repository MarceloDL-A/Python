#Para iniciar essa rotina deve se estar dentro de um diretório especificado e dentro desse diretório deve-se ter o subdiretório 'dados'
from os import chdir, getcwd #importa as funções para mudança de diretório chdir e para a informação do diretório atual getcwd
print('O diretório atual é', chdir('dados'), getcwd()) #muda para o diretório especificado (ex'dados') e informa qual o diretório atual
arq = open('Planetas-Texto.txt', 'w') #cria um arquivo vazio ('arq') e atribui um título.txt para esse arquivo ('Planetas-Texto.txt') usando a instrução para escrita do título 'w'
arq.write('1- Terra\n') #escreve ('Terra') no aquivo arq, salva o resultado e posiciona o cursor na próxima linha com o comando \n
arq.write('2- Marte \n3- Vênus\n') #muda de linha após escrever cada nome
arq.close() #fecha o arquivo arq
