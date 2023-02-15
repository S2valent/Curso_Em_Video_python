#Escreva um programa que leia um número interio qualquer, e peça para o usúario escolher qual será a base de conversão.
#-1 para binário
#-2 para octal 
#-3 hexadecimal
numero = int(input("Digite um número: "))
print('Escolha uma das bases para conversaão:\n[1] Binário\n[2] Octal\n[3] Hexadecimál')
escolha = int(input("sua opção:"))
if escolha == 1:
    print("{} convertido para Binário é {}".format(numero,bin(numero)[2:]))
elif escolha == 2:
    print("{} convertido para Octal é {}".format(numero,oct(numero)[2:]))
elif escolha == 3:
    print("{} convertido para Hexadedimal é {}".format(numero,hex(numero)[2:]))
else:
    print("Opcão inválida")
