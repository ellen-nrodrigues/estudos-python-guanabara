import math

#forma normal que seria feito

#co = float(input('Qual o comprimento do cateto oposto?'))
#ca = float(input('Qual o comprimento do cateto adjacente?'))
#hi = (co ** 2 + ca ** 2) ** (1/2)

#print(f'A hipotenusa do triângulo é: {hi:.2f}')

#com a importação

co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
hi = math.hypot(co, ca)

print(f'A hipotenusa do triângulo é: {hi:.2f}')
