#Crie um programa que faça o computador jogar jokenpô com você.
import random 
print("{:=^40}".format('JOQUENPÔ'))
mao = input("Pedra,Papel, ou Tesoura:").upper()
cpu1 = ('Pedra')
cpu2 = ("Papel")
cpu3 = ("Tesoura")
lista = [cpu1,cpu2,cpu3]
resultado = random.choice(lista)
print("="*50)
if (resultado == 'Pedra' and mao == 'PAPEL'):
    print("Eu escolho {} computador escolhe {}\nEu ganhei, uuuhhhhhuullll, papel engolhe a pedra!!!!".format(mao,resultado))
elif resultado == 'Papel' and mao == 'TESOURA':
    print("Eu escolho {} compitador escolhe {}\nEu ganhei tesoura corta papel uuuhuuuulllll!!!1".format(mao,resultado))
elif resultado == 'Tesoura' and mao == 'PEDRA':
    print("Eu escolho {} computador escolhe {}\nEu ganhei, Pedra quebra tetoura uuuhhhuuullll!!!1".format(mao,resultado))
elif (resultado == 'Pedra' and mao == 'PEDRA') or (resultado == 'Tesoura' and mao == "TESOURA") or (resultado == 'Papel' and mao == "PAPEL"):
    print('Empate!!! Eu escolhi {} e o computador escolheu {}.'.format(mao,resultado))
else:
    print("Eu escolho {} computador escolhe {}\nO computador ganhou roubado!! srrrrsrsrsrsrsrs".format(mao,resultado))

