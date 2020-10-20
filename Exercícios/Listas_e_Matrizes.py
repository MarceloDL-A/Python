from os import chdir, getcwd
import numpy as np
print('O diretório atual é: ', chdir('dados'), getcwd())
#Criação de um arquivo .txt formatado
import pandas as pd
arq = pd.read_csv('document.txt', sep='\t', header=[3], index_col=0)
#sep='\t' estabele que o sepação 'sep=' é do tipo tabulação '\t'
#header=[3] ignora as três primeiras linhas do arquivo e a próxima linha considerada a que possui os título da tabela
#index_col=0 especifíca qual coluna será utilizada como um índice posicionado à esquerda. Por default a coluna à esquerda fica numerada automaticamente.
print('Otipo do arquivo arq é: \n',  type(arq), len(arq))
print('Um exemplo de dado do arquivo é: \n', arq.columns, len(arq.columns))
mt0 = np.array(arq)
print('Experimento 01:', mt0)
print('Experimento 01B:', mt0[1][2])
mt = []
i = 0
k = 0
print('IndiceAAAAAA:', arq.index[2][0:])
while i < len(arq.columns):
    b = arq.columns[k]
    c01 = arq[b].tolist()
    mt.append(c01)
    print('teste', i, mt)
    i +=1
    k +=1
mtt = np.array(mt).T
print('BBBBBBBBB', mtt)
print('BBBBBBBB22222', mtt[0][2])
print(arq)
print('Matriz (coluna, linha) =', mt[0][4], mt[0][4]*mt[0][4])
print('Experimento 2: \n ====================')
mt2 = []
j = 0
l = 0
while j < len(arq):
    print('Imprime:', arq.index[j])
    j +=1
print('A matrix mt2 é: \n >>>>>>>>> \n', mt2)
#print('A primeira coluna será tranforma na lista c01:', c01)
p = c01[0]*c01[1]*c01[2]*c01[3]
print('O produto dos 4 primeiros termos da lista é:', p)
#df=pd.read_csv('document.txt',engine='python',sep='\s')
#print(df)
#tabela = pd.read_fwf("InAs.txt", delimiter="")
#print ('A tabela é:', tabela)

