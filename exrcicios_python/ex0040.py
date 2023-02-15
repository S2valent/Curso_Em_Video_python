# Crie um programa que leia duas notas de um aluno e calcule sua media,mostrando uma mensagem no final, de acordo com a média do atingida.
# - Média abaixo de 5 Reprovado.
# - Média entre 5 e 6.9 Recuperação.
# - Media 7 ou superior Aprovado.
n1 = float(input("Informe a primeria nota do aluno: "))
n2 =  float(input("Informe a segunda nota do aluno: "))
media = (n1+n2)/2
if media < 5:
    print("Você está reprovado!!!")
elif media >= 5 or media < 6.9:
    print("Estude mais, você está de recuperção!!!")
elif media > 7:
    print("Prabéns você esta aprovado!!!")
    