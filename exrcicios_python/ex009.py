#Faça um programa que leia um número interiro e mostre a sua tabuada#
numero = int(input('Informe um número: \n'))

for i in range(1,11):
    mult = i*numero
    print('{} x {} = {}'.format(i,numero,mult))
    