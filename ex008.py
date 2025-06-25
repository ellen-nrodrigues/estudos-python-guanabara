m = float(input('Uma distancia em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'A medida de {m} metros, tem:')
print(f'{km} km \n{hm} hm \n{dam} dam \n{dm} dm')
print(f'{cm:.0f}cm \n{mm:.0f}mm')
