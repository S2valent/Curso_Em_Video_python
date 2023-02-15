#Um porfessor quer sortear um dos seus 4 alunos para apagar o quadro.Faça um programa que ajude a ele, lendo o nome dele e  escrevendo o nome escolhido.#

import random 
n1 = str(input('Digite o nome: '))
n2 = str(input('Digite outro nome: '))
n3 = str(input('Digite outro nome: '))
n4 = str(input('Digite outro nome: '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
