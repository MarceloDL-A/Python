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
mt = np.array(arq) #trasforam o arquivo numa matriz
print('Experimento 01: \n', mt)
print('Experimento 01B:', mt[1][2])

#checagem dos termos da matriz
i = 0
while i < len(arq):
    j = 0
    while j < len(arq.columns):
        print('O valor da posição (i={},j={})'.format(i+1,j+1),'é', mt[i][j])
        j += 1
    i += 1
print('Experimento 03 \n:', mt)
arq2 = np.array(mt)
np.savetxt('Matrix002.txt', arq2.append, fmt='%.0f\t')