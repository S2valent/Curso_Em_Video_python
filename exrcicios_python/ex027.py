#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite o seu nome: ')).strip()
strings = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(strings[0]))
print('Seu ultimo nome é {}'.format(strings[len(strings)-1]))
      