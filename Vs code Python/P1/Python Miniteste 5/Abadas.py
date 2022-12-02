print("Bem-vindo")

comissarios = int(input("Houveram quantos comissários? "))
listaDeVendas = []

for i in range(comissarios):
    i = i + 1
    vendas = (input("Quantas vendas o", str(i),"º teve? "))
    listaDeVendas.append(vendas)

