#Escreva um programa que leia dois números  inteiros e compare-os,mostrando na tela uma mensagem:
# - O primeiro  valor é maior
# - O segundo valor é maior 
# - Nao existe maior os dois são iguais.
numero = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))
print("-"*90)
if numero > numero_2:
    print("O primeiro valor é maior, {} é maior que {}".format(numero,numero_2))
elif numero_2 > numero:
    print("O segundo valor é maior, {} é maior que {}".format(numero_2,numero))
else:
    print("Não existe maior os dois são iguais, {} = {}".format(numero,numero_2))
print("-"*90)
