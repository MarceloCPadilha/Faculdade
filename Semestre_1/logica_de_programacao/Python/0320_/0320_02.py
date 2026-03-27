'''
2. Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas
variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa. Mostrar o
conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.
'''

vA, vB = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))

print("vA = {} vB = {}".format(vA, vB))

vA ^= vB
vB ^= vA
vA ^= vB

print("vA = {} vB = {}".format(vA, vB))
