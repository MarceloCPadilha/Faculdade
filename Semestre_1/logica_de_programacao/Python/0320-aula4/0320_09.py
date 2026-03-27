'''
9. Faça um algoritmo que mostre o resultado da expressão abaixo:
(( x – 5) * y) – z
Obs: Ler valores para as variáveis x, y e z
'''
x, y, z = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))

resultado = ((x - 5) * y) - z

print("O resultado de ((x - 5) * y) - z = {}".format(resultado))
