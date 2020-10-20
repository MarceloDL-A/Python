from os import chdir, getcwd
print('O novo diretório é:', chdir('dados'), getcwd())
arq = open('Planetas-Texto.txt', 'r') #abre o 'arq' somente para leitura 'r'
while True: #abr um laço que que executara (se o parametro for 'True' executará indefinidamente) os comando com espaçamento colocados abaixo até a condição do laço não for mais satisfeita ou até um comando 'break' for executado
    linha = arq.readline() #lê uma linha do 'arq'
    if linha == "": #dá uma condição para que os comandos espaçados abaixo sejam executadas
        break #comadno executado se a condição escrita na linha if for obedecida
    print(linha, end="") #caso a condição do 'if' não seja obedecida imprime a linha na rela com uma instrução para o cursor ir para a próxima linha, ou usa-se end="" para não adicionar a nova linha
arq.close() #quando o comando 'break' for executado o loop 'while' termina e 'arquivo.close()' é executado
arq = open('Planetas-Texto.txt', 'r') #reabre o arquivo
linhas = arq.readlines() #lê todas as linhas
print(linhas)
arq.close()