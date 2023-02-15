#Faça um programa que leia um ano qualquer e mostre se ele é ano Bissexto.
from calendar import isleap
ano = int(input('Digite um ano: '))

if isleap(ano):
    print('O ano {} é Bissesto'.format(ano))
else:
    print('O ano {} não é Bissesto.'.format(ano))
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0 :
    print('Ano {} é Bissexto'.format(ano))
else:
     print("O ano não {} é Bissexto".format(ano))
