p1 = float(input('Qual é o preço do produto? \n'))
d = float(input('Qual é o percetual de desconto? \n'))
p2 = p1*((100-d)/100)
print('O valor do produto com desconto é {} reais'.format(p2))