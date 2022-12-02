print("==Bem-vindo==")
print("==Saiba o quanto foi gasto para lavar as roupas de 5 listas==")

print("lavanderia oferece ao cliente duas opções de cobrança: R$ 7,00 por peça de roupa ou R$5,00 por quilo.")
print("Caso a lavagem seja a seco, é acrescentada uma taxa de R$ 3,50.")

contadorLista = 0
for i in range(5):
    contadorLista += 1
    print("==lista " + str(contadorLista) + "==")
    tipoDeCobrancaLista = int(input("Qual o tipo de lavagem? Digite 1 se for por peça ou digite 2 se for por quilo: "))
    
    if tipoDeCobrancaLista == 1:
        numeroDeRoupas = int(input("Diga quantas roupas são: "))
        pagamento = float(numeroDeRoupas * 7)
        tipoDeLavagemLista = int(input("A lavagem é à seco? Digite 1 se sim ou 2 se não: "))
        
        if tipoDeLavagemLista == 1:
            pagamento += 3.50
            print("A lista " + str(contadorLista) + " custou: R$" + str(pagamento))
            
        elif tipoDeLavagemLista == 2:
            print("A lista " + str(contadorLista) + " custou: R$" + str(pagamento))
        else:
            print("Opção inválida.")
    elif tipoDeCobrancaLista == 2:
        numeroDeRoupas = int(input("Diga quantas roupas são: "))
        totalDoPeso = 0
        contador = 1    
        
        for i in range(numeroDeRoupas):
            pesoDaRoupa = int(input("Digite o peso da roupa em gramas: "))
            totalDoPeso += pesoDaRoupa
            contador += 1
        
        tipoDeLavagemLista = int(input("A lavagem é à seco? Digite 1 se sim ou 2 se não: "))
        pagamento = float(totalDoPeso / 1000 * 5)

        if tipoDeLavagemLista == 1:
            pagamento += 3.50
            print("A lista " + str(contadorLista) + " custou: R$" + str(pagamento))
        else:
            print("A lista " + str(contadorLista) + " custou: R$" + str(pagamento))
    else:
        print("Opção inválida.")
        
    pagamentoTotal = 0
    pagamentoTotal += pagamento

print("O valor total a ser pago é R$" + str(pagamentoTotal))
print("Fim do programa.")

