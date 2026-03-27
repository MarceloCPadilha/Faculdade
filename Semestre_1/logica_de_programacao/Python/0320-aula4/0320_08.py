'''
8. Faça um algoritmo que leia valores para as variáveis a, b e c e mostre o resultado da seguinte
expressão:
( a – b ) * c
'''

a, b, c = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))

resultado = (a - b) * c

print("O resultado de (a - b) * c = {}".format(resultado))
