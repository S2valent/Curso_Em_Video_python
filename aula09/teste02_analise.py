#Análise da frase python #
frase = 'Leandro Ponciano'
print(frase.count('o'),'----O python vai mostar quantas vezes a leta (o) apareceu, ele diferencia a letra maiúscula da minúscula \n')
print(len(frase),'O python vai mostrar quantos caracteres tem ou seja quantos espaços \n ')
print(frase.upper().count('O'),' -----O vai python vai  colocar a letra maiúscula. \n')
print(frase.replace('Ponciano','Oliveira'),'O python só vai printar na tela mas não vai salvar \n')
#Da forma abaixo o python vai printar mas também vai salvar na memória#
frase = frase.replace('Ponciano','Oliveira')
print(frase)
#desconbrido se a palavra esta dentro da frase vai retornar false ou true#
print('Leandro' in frase)
print(frase.split(),'------O python vai separar as duas as frases entre conchetes\n')
dividido = frase.split()
print(dividido[1],'-------O python vai printar a string 1 \n')
print(dividido[1][2],'-----O python vai  mostrar a  string 1 e a letra na posição 2 \n')



