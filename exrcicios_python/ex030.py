# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
numero = int(input('Digite um número: '))
if numero %2 == 0:
    print('Você digitou {} e o numero é par'.format(numero))
else:
    print('Você digitou {} e o número é impar'.format(numero))