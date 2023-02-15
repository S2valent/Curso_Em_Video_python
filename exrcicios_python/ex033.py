#Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digte um número: '))
n3 = int(input('Digite um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print("{} é o menor número".format(menor))
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print("{} é o  maior número".format(maior))