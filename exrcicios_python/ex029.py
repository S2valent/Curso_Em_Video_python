# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa voi custar R$7,00 por cada km acima do limite.
velocida = int(input('Digite a velocidade : '))
multa = (velocida-80)*7
if velocida > 80:
    print('Você estava acima da velocida e vai pagar uma multa no valor de R${} equivalente a R$7.00 a cada Km/h acima da velocidade permitida!!'.format(multa))

