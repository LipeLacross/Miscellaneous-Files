print("==Bem-vindo==")
print("==Saiba o quanto foi gasto para lavar as roupas de 5 listas==")

print("lavanderia oferece ao cliente duas opções de cobrança: R$ 7,00 por peça de roupa ou R$5,00 por quilo.")
print("Caso a lavagem seja a seco, é acrescentada uma taxa de R$ 3,50.")

contadorLista = 0
pagamentoTotal = 0
quantidadeDeLavangensASeco = 0

for i in range(5):
    contadorLista += 1
    print("==lista " + str(contadorLista) + "==")
    tipoDeCobrancaLista = int(input("Qual o tipo de lavagem? Digite 1 se for por peça ou digite 2 se for por quilo: "))
    
    if tipoDeCobrancaLista == 1:
        numeroDeRoupas = int(input("Diga quantas roupas são: "))
        pagamento = float(numeroDeRoupas * 7)
        tipoDeLavagemLista = int(input("A lavagem é à seco? Digite 1 se sim ou 2 se não: "))
        
        if tipoDeLavagemLista == 1:
            quantidadeDeLavangensASeco += 1
            pagamento += 3.50
            print("A lista " + str(contadorLista) + " custou: R$" + str(pagamento))
            
        elif tipoDeLavagemLista == 2:
            print("A lista " + str(contadorLista) + " custou: R$" + str(pagamento))
        else:
            print("Opção inválida.")
            break
    elif tipoDeCobrancaLista == 2:
        pesoDasRoupas = float(input("Diga qual é o peso total em kg: "))
        tipoDeLavagemLista = int(input("A lavagem é à seco? Digite 1 se sim ou 2 se não: "))
        pagamento = float(pesoDasRoupas * 5)

        if tipoDeLavagemLista == 1:
            quantidadeDeLavangensASeco += 1
            pagamento += 3.50
            print("A lista " + str(contadorLista) + " custou: R$" + str(pagamento))
        elif tipoDeLavagemLista == 2:
            print("A lista " + str(contadorLista) + " custou: R$" + str(pagamento))
        else:
            print("Opção inválida.")
            break
    else:
        print("Opção inválida.")
        break
        
    pagamentoTotal += pagamento

print("O valor total a ser pago à lavanderia é R$" + str(pagamentoTotal))
print("Houveram " + str(quantidadeDeLavangensASeco) + " lavagens à seco."  )
print("Fim do programa.")



