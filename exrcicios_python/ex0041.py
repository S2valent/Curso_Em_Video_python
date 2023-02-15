# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Júnior
# - Até 20 anos: Sênior
# - Acima Master
from datetime import date
nascimento = int(input("Informe a data de nascimento do atleta: "))
ano_atual = date.today().year
idade =  ano_atual- nascimento
print("="*40)
if  idade <= 9:
    print("Sua categoria é Mirin!!")
elif idade > 9 and idade <= 14:
    print("Sua categoria é Infantil!!")
elif idade >14 and idade <= 19:
    print("Sua categoria é Júnior!!!")
elif idade > 19 and idade <=20:
    print('Sua categoria é Sênior!!')
else:
    print("Sua categoria é Master!!")
print("Seja bem vindo!!!")
print("="*40)
    