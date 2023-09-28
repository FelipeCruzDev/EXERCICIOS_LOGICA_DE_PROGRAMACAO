'''
As maçãs custam R$ 1,30 cada se forem
compradas menos de uma dúzia, e R$ 1,00
se forem
compradas pelo menos 12. Escreva um
programa que leia o número de maçãs
compradas, calcule e
escreva o custo total da compra
'''
macacomp= int(input("Informe quantas maçãs você comprou: "))

if macacomp < 12:
    valortotal=macacomp*1.30
    print("O VALOR TOTAL DA COMPRA FOI DE R${} ".format(valortotal))
else:
    valortotal=macacomp*1.00
    print("O VALOR TOTAL DA COMPRA FOI DE R${} ".format(valortotal))