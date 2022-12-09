import miniteste5bib

print("Bem-vindo")

listaDeVendas = []
listaDeRecompensa = []
contadorDeComissarios = 0
vendasTotais = 0
contadorBonus = 0

while True:
    venda = int(input("Quantas vendas esse comissários teve? (para parar digite 0) "))
    vendasTotais += venda 
    if venda > 0:
        contadorDeComissarios += 1
    else:
        break
    listaDeVendas.append(venda)

for i in range(contadorDeComissarios):
    c = listaDeVendas[i]
    recompensa = miniteste5bib.calculaComissao(c)
    bonus = miniteste5bib.calculaBonus(c)
    if bonus == 70:
        contadorBonus += 1
    comissaoTotal = recompensa + bonus
    listaDeRecompensa.append(comissaoTotal)

maiorVenda = miniteste5bib.obtemMaior(listaDeVendas)
menorVenda = miniteste5bib.obtemMenor(listaDeVendas)

print("Aqui está a comissão em ordem, do primeiro até o último comissário declarados: ")

ordem = 0
for i in range(len(listaDeRecompensa)):
    ordem += 1
    print("Comissário", str(ordem),"deve receber", str(listaDeRecompensa[i]), "reais.")

print("Quantidade de bonus obtidos:", contadorBonus)
print("Quantidade de abadás vendidos:", vendasTotais)
print("Maior número de vendas entre os comissários:", maiorVenda)
print("Menor número de vendas entre os comissários:", menorVenda)


    