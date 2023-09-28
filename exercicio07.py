'''
Faça um código que receba o valor da
base e da altura de um triângulo e
calcule sua área. usando a fórmula A =
(base x Altura ) /2
(E QUE NAO ACEITE O NUMERO ( 0 ), NA BASE E ALTURA)
'''

base = float(input("DIGITE A BASE: "))
while base == 0:
    base = float(input("NUMERO IGUAL A 0, DIGITE NOVAMENTE A BASE: "))
    
altura = float(input("DIGITE A ALTURA: "))
while altura == 0:
    altura = float(input("NUMERO IGUAL A 0, DIGITE A ALTURA: "))

area = (base*altura)/2
print("A AREA DO TRIANGULO: {}".format(area))
