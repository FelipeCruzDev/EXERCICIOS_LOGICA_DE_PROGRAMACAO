'''Crie um algoritmo que receba 3
números e informe qual o maior entre
eles.'''
numero1 = int(input("informe um numero: "))
numero2 = int(input("informe um numero: "))
numero3 = int(input("informe um numero: "))
if numero1 > numero2:
    if numero1 > numero3:
        print("o {} é maior".format(numero1))
    else:
        print("o {} é maior".format(numero3))
elif numero2 > numero3:
    print("o {} é maior".format(numero2))
else:
    print("o {} é maior".format(numero3))