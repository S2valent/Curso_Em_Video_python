#Desenvolva um programa que pergunte a distância de um vaigem em Kilometro.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45  para viagens mais longas.
distancia = float(input('Informe a distância percorrida até seu destino: '))
if distancia <= 200:
    print('O valor a ser pago é R${}'.format(distancia * 0.50))
else:
    print('O valor as ser pago é R${}'.format(distancia * 0.45))