from os import chdir, getcwd
print('O diretório atual é:', chdir('dados'), getcwd())
#Criação de um arquivo .txt formatado
arq = open('MRUV-Texto.txt', 'w') #cria o arquivo 'arq' com o título 'MRUV'
a = 5. #o ponto força para o tipo float
t = 0. ; dt = 0.0002 # várive 't' que armazena um tempo inicial '0' e incremento 'dt'
while t <=2:
    x = a*t**2. #cálculo da posição
    arq.write('t = {0:.5} s \t x = {1:.3} m \n'.format(t, x))
    t+= dt #atualiza  variável 't' com o valor atual acrescido de 'dt'
arq.close() #fecha o arquivo
#Impressão na tela organizada do conteúdo do arquivo .txt formatado
arq = open('MRUV-Texto.txt', 'r') #abre o arquivo para leitura
while True: #Inicia um loop
    linha = arq.readline() #lê uma linha do arquivo 'arq'
    if linha == "": #executa as intruções abaixo se essa condição for obedecida
        break #sai do loop
    print(linha, end="") #imprime a linha
arq.close()
