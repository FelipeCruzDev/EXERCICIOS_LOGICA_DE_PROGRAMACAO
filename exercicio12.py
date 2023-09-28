'''
Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitore
'''

eleitores = int(input("DIGITE O NUMERO TOTAL DE ELEITORES: "))
votosb = int(input("DIGITE O NUMERO TOTAL DE VOTOS BRANCOS: "))
nulos = int(input("DIGITE O NUMERO TOTAL DE VOTOS NULOS: "))
validos = int(input("DIGITE O NUMERO TOTAL DE VOTOS VALIDOS: "))


respnul=(nulos/eleitores)*100
respbranco=(votosb/eleitores)*100
respvalido=(validos/eleitores)*100

print ("O TOTAL DE PESSOAS QUE VOTARAM FOI: {}% ".format(eleitores))
print ("O TOTAL DE VOTOS NULOS FOI: {}% ".format(respnul))
print ("O TOTAL DE VOTOS BRANCOS FOI: {}% ".format(respbranco))
print ("O TOTAL DE VOTOS VALIDOS FOI: {}% ".format(respvalido))