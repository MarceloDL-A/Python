from os import chdir, getcwd
print('O diretório atual é: ', chdir('dados'), getcwd())
#Criação de um arquivo .txt formatado
import pandas as pd
arq = pd.read_csv('document.txt', sep='\t', header=[3], index_col=0)
#sep='\t' estabele que o sepação 'sep=' é do tipo tabulação '\t'
#header=[3] ignora as três primeiras linhas do arquivo e a próxima linha considerada a que possui os título da tabela
#index_col=0 especifíca qual coluna será utilizada como um índice posicionado à esquerda. Por default a coluna à esquerda fica numerada automaticamente.
print('O tipo do arquivo arq é: \n',  type(arq))
print('Um exemplo de dado do arquivo é: \n', arq.columns)
i = 0
a = []
t=15
while i < 9:
    a.append(t)
    print('teste', i+1, a)
    i+=1

c01 = arq['Col 01'].tolist()
print('A primeira coluna será tranforma na lista c01:', c01)
p = c01[0]*c01[1]*c01[2]*c01[3]
print('O produto dos 4 primeiros termos da lista é:', p)
#df=pd.read_csv('document.txt',engine='python',sep='\s')
#print(df)
#tabela = pd.read_fwf("InAs.txt", delimiter="")
#print ('A tabela é:', tabela)