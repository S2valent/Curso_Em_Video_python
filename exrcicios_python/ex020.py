#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que  leia o nome dos quatro alunos e mostre a ordem sorteada.#

from random  import shuffle
nome_1 = input('Informe o nome do aluno : ')
nome_2 = input('Informe  nome do aluno : ')
nome_3 = input('Informe o nome do aluno: ')
nome_4 = input('Informe o  nome do aluno: ')
lista = [nome_1,nome_2,nome_3,nome_4]
shuffle(lista)
print('A sequência dos alunos')
print(lista)

