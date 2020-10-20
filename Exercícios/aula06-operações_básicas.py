n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
s = n1 + n2
m = n1*n2
d = n1/n2
di = n1//n2
r=n1%n2
e = n1**n2
print('A soma é {:.3f} \nProduto é {:.3f} \nA divisão é {:.3f} \nA divisão inteira é {:.0f} \nO resto da divisão é {'
      ':.0f} \nA potência é {:.3f}'.format(s, m, d, di, r, e))
