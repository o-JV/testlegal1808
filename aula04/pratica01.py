servicos = ["corte", "barba", "sobrancelha"]



for i, servicos in enumerate(servicos, start=1):
    print(i,servicos)


precos = [20.00, 15.00, 10.00]
total = 0

for preco in precos:
    total += preco
    print(f"Patrão, deu {total:.2f} reaizes!")

saldo = 200
quantidade_cortes = 0

while saldo >= precos[0]:
    saldo -= precos[0]
    quantidade_cortes += 1
print(f"Patrão, tu consegue cortar {quantidade_cortes} vezes!")