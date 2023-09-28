'''
Faça um código que receba 4
números e realize a soma deles e a
média entre eles. e mostre os
resultados.
'''
soma = 0
num = int(input("DIGITE A QUANTIDADE DE VEZES: "))
for x in range(num):
    n = int(input("DIGITE UM NUMERO: "))

    soma = soma + n
    media = soma/num

print ("A SOMA DEU: {} e média DEU {} ".format(soma,media))
