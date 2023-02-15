#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.#
numero = int(input('Informe um número:'))
dobro = numero+numero
triplo =  numero*3
raiz =  numero**(1/2)
print('O dobro é {}, o triplo é {}, a raiz quadrada é {}'.format(dobro,triplo,raiz))