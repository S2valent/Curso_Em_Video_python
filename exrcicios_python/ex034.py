#Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salários superiores para R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais o aumento é de 15%.
salario = float(input('Informe o salário do funcionario: R$'))
if salario >= 1.250:
    novo_s = (salario*15/100)+salario
    print('Você recebeu um bonus de 10%, seu novo salário é R${:.2f}'.format(novo_s))
else: 
    salario < 1.250
    novo_s = (salario*10/100)+salario
    print('Você recebeu um bonus de 15%, seu novo salário sera R${:.2f}'.format(novo_s))
    
