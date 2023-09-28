'''Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente'''

num1 = int(input("INFORME UM VALOR: "))
num2 = int(input("INFORME UM VALOR: "))

if num1 < num2:
    print("{},{}".format(num1,num2))
else:
    print("{},{}".format(num2,num1))