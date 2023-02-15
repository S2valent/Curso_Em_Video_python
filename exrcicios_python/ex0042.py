#Refaça o desafio ex0035 dos triângulos, acrescentando o recurso de mostrar qual tipo de triângulo sera formado.
l1 = int(input('Informe a primeira reta:' ))
l2 = int(input("Informe a segunda reta: "))
l3 = int(input("Informe a terceira reta: "))
print("-"*60)
if l1==l2 and l2==l3:
    print("É um Triângulo Equilátero, os três lado são iguais!!")
elif ((l1==l2 and l3 != l2) or (l2==l3 and l3!= l1) or (l1==l3 and l3!=l2)):
    print("É um Triângulo Isósceles, dois lados iguais!!")
else:
    print("É um triângulo Escaleno, todos os lados são diferentes!!")
print("-"*60)