#Faça um programa que leia um número que vai de 0 até 9999 e mostre na tela cada um dos digitos separados#
print('STRING')
numero = (input('Digite um número entre 0 e 9999: '))
numero = numero.rjust(4,'0')
milhar,centena,dezena,unidade = numero
print(f'{unidade =}\n{dezena =}\n{centena =}\n{milhar =}')
print('\n MATEMÁTICA')
numero = int(input('Digite um número entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analizando o número {}'.format(numero))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

