'''
Natália abriu uma loja de bijuterias recentemente e as vendas vão muito bem. 
Pensando em atrair uma clientela ainda maior, 
ela deseja oferecer um desconto de 10% para os clientes q
ue gastarem R$ 100,00 ou mais e pagarem em dinheiro. 
Escreva um programa que receba como entrada o valor do produto comprado 
e a forma de pagamento escolhida (dinheiro ou cheque), 
calcule o desconto devido (caso necessário), e exiba o valor final a ser pago.

Dados de entrada para teste:

Valor 80
Forma Pagamento Dinheiro
R$ 80.00

Valor 120
Forma Pagamento Cheque
R$ 120.00

Valor 100
Forma Pagamento Dinheiro
R$ 90.00

Valor 70
Forma Pagamento Cartão
Forma de pagamento inválida
'''

print("====Loja de Natália====")#by Felipe Moreira

carrinho = float(input("Qual o valor da compra? "))

if carrinho <= 0:
    print("Valor inválido!!!")
else:
    formaDePagamento = int(input("Digite 1 se for usar dinheiro, 2 se for cheque ou 3 se for cartão: "))
    
    if formaDePagamento == 1:
        if carrinho >= 100:
            print("O valor é R$", (carrinho - carrinho * 10/100), '(Descontado 10%)')
        else:
            print("O valor é R$", carrinho)
    elif formaDePagamento == 2:
        print("O valor é R$", carrinho)
    elif formaDePagamento == 3:
        formaDePagamentoCartao = int(input("Digite 1 se for crédito ou 2 se for débito: "))
        if formaDePagamentoCartao == 1:
            vezes = int(input("Quantas vezes?(Máximo 3 vezes) "))
            if vezes > 0 and vezes <= 3:
                    print("O valor é", vezes, "vezes de R$", (carrinho / vezes))
            else:
                print("Parcelamento inválido!!!")
        elif formaDePagamentoCartao == 2:
            print("O valor é R$", carrinho)
        else:
            print("Operação inválida!!!")
    else:
        print("Forma de pagamento inválida!!!")
