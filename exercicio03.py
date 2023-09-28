'''Crie um código que leia a idade de
uma pessoa e diga em qual ano ela
nasceu'''

idade = int(input("DIGITE SUA IDADE: "))
ano = int(input("QUAL O ANO ATUAL: "))
mesatual = int(input("DIGITE O MES ATUAL (DE 1 a 12): "))
mesnasc = int(input("DIGITE O MES QUE VOCE NASCEU (DE 1 a 12): "))
nascimento = ano - idade
if mesnasc >= mesatual:
    nascimento = ano-idade-1
else:
    nascimento = ano - idade

print("O ANO QUE VOCE NASCEU FOI:  {} ".format(nascimento))