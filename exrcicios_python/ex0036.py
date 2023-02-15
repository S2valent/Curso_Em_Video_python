#Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo sera negado.
salario = float(input("Informe o seu salário : R$"))
casa = float(input("Informe o valor da casa que deseja financiar: R$"))
anos_pg = int(input("Em quantos anos vc quer pagar o financiamento: "))
mensal = anos_pg*12
valor_prestacao = casa/mensal
entrada = casa - (salario*30/100)*mensal
print("="*100)
if valor_prestacao > (salario * 30/100):
    print("Que pena seu empréstimo foi negado\nO valor da prestação não pode exceder 30 porcento do seu salário. \nSerá necéssario dar uma entrada de R${:.3f}.".format(entrada))
elif valor_prestacao < (salario*30/100):
    print("Parabéns o seu financiamento foi aprovado, procure o banco do Brasil para finalizar o financiamento!!!")
    print("Sua prestação será de  {:.3f}".format(valor_prestacao))
print("="*100)


 