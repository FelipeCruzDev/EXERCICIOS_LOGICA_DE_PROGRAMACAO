ano = int(input("Escreva sua idade: "))
meses = int(input("Escreva mês que você nasceu: "))
dias = int(input("Escreva o dia que você nasceu: "))

diatotal= (ano*365)+(meses*30)+dias

print("Sua idade em dias é: {} ".format(diatotal))