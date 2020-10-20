from os import getcwd, chdir, mkdir
print('O diretório de trabalho atual é \n' + getcwd(), '\n')
#print('Digite o novo diretório:')
#chdir(r'C:\Users\PCMBE\Desktop\M\0D\Python_arquivos_criados')
n = input('Digite o nome do novo diretório a ser criado:\n')
mkdir(n) #Cria novos diretórios
chdir(n) #Muda de diretórios
print('O diretório atual é: \n' + getcwd(), '\n')
arquivo = open('Planetas-Sequencial', 'a')
print('Um arquivo foi criado e aberto para inserção de dados no diretório atual. \n')
i = int(input('Quantas palavras você quer inserir no arquivo? \n'))
for k in range(0, i):
    n1 = input('Escreva o nome de um planeta: \n')
    arquivo.write(n1)
arquivo.close() #fecha o arquivo

