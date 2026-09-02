servicos = ["corte", "barba", "sobrancelha"]


for i, servicos in enumerate(servicos, start=1):
    print(i, servicos)


precos = [25.00, 18.00, 10.00]
total = 0


for preco in precos:
    total =+ preco
    print(f"o valor deu {total:.2f}R$")

saldo = 200
quantidade_cortes = 0

while saldo >= 200:
    saldo -= precos(0)
    quantidade_cortes +=1
print(f"voce consegue fazer {quantidade_cortes} vezes! sobrou R${saldo}:.2f")