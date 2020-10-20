import sympy as sp
x = sp.Symbol('x')
fp = input('Digite a função para obter a sua primitiva: \n')
print('A primitiva é:')
print(sp.integrate(fp , x))
x1 = float(input('Qual o limite inferior de integração? \n'))
x2 = float(input('Qual o limite superior de integração? \n'))
print('A integral avaliada entre {} e {} é:'.format(x1, x2))
def f(x):
    return 6*x**2 + 2
from scipy.integrate import quad
res, err = quad(f, x1, x2)
print(res)
print('O erro é:')
print(err)



