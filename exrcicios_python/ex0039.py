# Faça um programa que que leia o ano de nascimento de um jovem, de acordo com sua idade.
# - Se ele ainda vai se alista ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# - Seu  programa também devera mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nascimento = int(input('Informe o ano de nascimento: '))
idade = atual - nascimento
tempo1 = idade - 18
tempo = 18 - idade
print("="*50)
if idade < 18:
    print("Quem nasceu em {} tem {} anos.\nAinda não está na hora de se alistar.\nFaltam ainda {} anos  para se alistar.".format(nascimento,idade,tempo))
elif idade == 18:
    print("Quem nasceu em {} tem {} anos.\nPor favor procuro o local de alistamento para se inscrever!!".format(nascimento,idade,tempo1))
elif idade > 18:
    print("Quem nasceu em {} tem {} anos.\nJá passou da hora de se alistar, Você está atrasado {} anos ,procure o local de alistamento.".format(nascimento,idade,tempo1)) 
print("="*50) 
