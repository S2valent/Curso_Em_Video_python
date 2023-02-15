#Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'#
cidade = input('Informe o nome da cidade:').strip()
true_false = cidade.split()
print('SANTO' in true_false[0].upper())