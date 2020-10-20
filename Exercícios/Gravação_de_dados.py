from os import chdir, getcwd
import pickle #importa o módulo para preservação de dados
print('O diretório atual é:', chdir('dados'), getcwd())
#Criação de um arquivo .txt formatado
arq = open('MRUV-Preservado.txt', 'wb') #cria o arquivo 'arq' com o título 'MRUV'
a = 5. #o ponto força para o tipo float
t = 0. ; dt = 0.0002 # várive 't' que armazena um tempo inicial '0' e incremento 'dt'
while t <=2:
    x = a*t**2. #cálculo da posição
    pickle.dump([t, x], arq)
#    arq.write('t = {0:.5} s   x = {1:.3} m \n'.format(t, x))
    t+= dt #atualiza  variável 't' com o valor atual acrescido de 'dt'
arq.close() #fecha o arquivo
#Impressão na tela organizada do conteúdo do arquivo .txt formatado
arq = open('MRUV-Preservado.txt', 'rb') #abre o arquivo para leitura
while True: #Inicia um loop
    par = pickle.load(arq)
    print(par)
arq.close()
