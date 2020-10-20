from os import chdir, getcwd
import pickle #importa o módulo para preservação de dados
print('O diretório atual é:', chdir('dados'), getcwd())
#Criação de um arquivo .txt formatado
arq = open('MRUV-Preservado.txt', 'rb') #abre o arquivo 'arq' com o título 'MRUV' para leitura 'rb'
print('MRUV com a = 5 m/s**2') #Imprime um título
print(arq)
dados = [] #esta linha '[]' vai receber os dados
print('CHECK')
while True: #laço de leitura dos dados
    try: #tenta ler um par t, x
        dados.append(pickle.load(arq))
    except: #quando chega no final do arquivo
        break #sai do laço
arq.close() #fecha o arquivo 'arq'
for i in range(1, len(dados)): #entra num loop para manipular os dados lidos por 'len'
    ti, tf = dados[i-1][0], dados[i][0] #os dados são números com os quais pode-se fazer diretamente um cálculo numérico
    #os dos 'ti' e 'tf' são tempos sucessivos da primeira coluna -[i][0] significa: linha=>[i] e coluna => [0]- começando por i=1 para resultar no tempo da primeira linha ti=[0][0]
    dx = dados[i][1]-dados[i-1][1] #armazena os dados da segunda coluna [i][1] em 'dx'
    print('No intervalo entre {0:.3} s e {1:.3} s, o deslocamento foi de {2:.3} m'.format(ti, tf, dx)) #impressão dos resultados
