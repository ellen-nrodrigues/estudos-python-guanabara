import math

an = float(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(an))
print(f'O ângulo de {an} tem o seno de {se:.2f}')
co = math.cos(math.radians(an))
print(f'O ângulo de {an} tem o cosseno de {co:.2f}')
tan = math.tan(math.radians(an))
print(f'O ângulo de {an} tem a tangente de {tan:.2f}')