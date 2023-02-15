from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de nascimento:'))
idade = atual - ano
print("Se você nasceu em {} você tem {} anos ".format(ano,idade))