'''um código que leia um número
diferente de zero e diga se este número
é positivo ou negativo'''

n = int(input("digite um numero: "))
while n ==0:
    if n == 0:
        n = int(input("NUMERO INVALIDO,digite um numero: "))
    elif n > 0:
        print("NUMERO POSITIVO")
else:
    print ("NUMERO NEGATIVO")