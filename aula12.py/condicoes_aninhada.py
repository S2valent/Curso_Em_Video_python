nome = str(input("Informe seu nome: "))
if nome == 'Leandro':
    print("Que nome lindo vc tem!!")
elif nome == 'Marta' or nome ==  'Maria' or nome == 'josé':
    print("Que nome comum vc tem!!")
elif nome in 'paulo andre marcos vithor':
    print('vc será bem sucedido na vida!!!')
print("Seja bem vindo {}!!".format(nome))
