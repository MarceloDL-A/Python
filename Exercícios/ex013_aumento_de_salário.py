p1 = float(input('Qual é o valor do salário do funcionário? \n'))
d = float(input('Qual é o percetual de aumento? \n'))
p2 = p1*((100+d)/100)
print('O valor do salário com aumento é de R${:.2f}'.format(p2))