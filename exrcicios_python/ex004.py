#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.#
algo = input('Digite algo:')
print('O tipo primitivo é',type(algo))
print('Só tem espaços? ',algo.isspace()) 
print('É um número?',algo.isnumeric())
print('É alfáberico ?',algo.isalpha())
print('É alfanumerico?',algo.isalnum())
print('Esta em maiúsculo?',algo.isupper())
print('Está em minúsculo?',algo.islower())
print('Está capitalizado?',algo.istitle())