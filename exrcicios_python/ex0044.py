#Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
# - Ávista dinheiro/chegue: 10% de desconto.
# - Ávista no cartão: 5% de desconto.
# - Em até 2 vezes no cartão preço normal.
# - 3 vezes ou mais 20% de juros.
print("{:=^40}".format('PRO_GAMER'))
produto = float(input("Informe o valor do produto:R$ "))
pagamento = int(input(''' FORMAS DE PAGAMENTO
[1] á vista dinheiro/chegue
[2] á avista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão\nQual é a opção?'''))
print("="*80)
if pagamento == 1 :
    print("O valor do produto é R${}".format(produto-(produto*10/100)))
elif pagamento == 2:
     print("O valor do produto é R${}".format(produto-(produto*5/100)))
elif pagamento == 3:
    print("O valor do produto R${} sem juros.".format(produto))
elif pagamento == 4:
    total_parcelas = int(input('Quantas parcelas?'))
    print('Sua compra será parcelada em {}X'.format(total_parcelas))
    print("Sua compra de {:.2f} vai custar {:.2f} no final das {} parcelas.".format(produto,produto+(produto*20/100),total_parcelas))
else:
    pagamento == 0
    print("Opção inválida.")
     