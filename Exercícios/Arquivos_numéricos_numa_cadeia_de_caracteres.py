from os import chdir, getcwd
print('O diretório atual é:', chdir('dados'), getcwd())
arq = open('MRUV', 'w') #cria o arquivo 'arq' com o título 'MRUV'
a = 5. #o ponto força para o tipo float
t = 0. ; dt = 0.2 # várive 't' que armazena um tempo inicial '0' e incremento 'dt'
while t <=2:
    x = a*t**2/2. #cálculo da posição
    arq.write(str(t)) #grava o tempo em 'arq'
    arq.write(str(x)) #grava a posição em 'arq'
    t+= dt #atualiza  variável 't' com o valor atual acrescido de 'dt'
arq.close() #fecha o arquivo
arq = open('MRUV', 'r') #abre o arquivo para leitura
print(arq.read()) #lê todo o arquivo 'arq' e impime seu conteudo
arq.close()
