servicos = ["corte", "barba", "sobrancelha"]
precos = [20.00, 15.00, 10.00]
total = 0




for i, servicos in enumerate(servicos, start=1):
    print(i,servicos)

for preco in precos:
    total += preco
    print(f"Irmão, deu  R${total}") 

    saldo = 200
    quantidade_cortes = 0

    while saldo >= precos[0]:
        saldo -= precos[0]
        quantidade_cortes += 1
    print(f"tu consegue cortar: R${quantidade_cortes} vezez!!")
