#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo coma tabela abaixo.
# - Abaixo de 18.5 : abaixo do peso.
# - Entre 18.5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - Acima de 40 obesidade morbida
altura = float(input('Informe a sua altura: (KG)'))
peso = float(input("Por favor Digite seu peso:(M) "))
imc = peso/(altura**2)
print('='*100) 
if imc < 18.5:
    print("Seu IMC é {:.f}\nVocê esta abaixo do peso ideal.".format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f}\nParabéns, vc está com peso ideal!!'.format(imc))
elif imc > 25 and imc <= 30:
    print("Seu IMC é {:.1f}\nVocê esta com sobrepeso, cuidade de sua saúde!!!!".format(imc))
elif imc > 30 and imc <= 40:
    print("Seu imc é {:.1f}\nCuidado você está com obesidade, cuide de sua saúde!!!".format(imc))
else:
    print("seu IMC esta acima de  40.\n PROCURE ORIENTAÇAO MÉDICA COM URGÊNCIA!!")
print("="*100)


