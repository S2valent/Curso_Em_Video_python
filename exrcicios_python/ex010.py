#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.#
carteira = float(input('Quanto você tem na cartteira? '))
dolar = 3.27
pode_comprar = carteira // dolar
print('Você pode comprar US$$ {} dolares'.format(pode_comprar))



