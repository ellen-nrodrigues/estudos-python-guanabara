d = int(input('Quantos dias alugado? '))
k = float(input('Quantos quilometros rodados? '))
total = (60.0 * d) + (0.15 * k)
print(f'O total a pagar é R${total:.2f}')