p = float(input('Qual é o preço do produto? '))
d = p - (p * 5 / 100)
print(f'O produto que custava R${p}, na promoção com desconto de 5% vai custar R${d:.2f}')