#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.#
salario = float(input('Informe o salário do funcionário: R$'))
Novo_Salario = salario + (salario*15/100)

print('\n Salário do funcionário: R${}'.format(salario))
print('\n Salário com bonus de 15%: R${}'.format(Novo_Salario))
