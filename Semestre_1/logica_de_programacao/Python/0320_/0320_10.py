'''
Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.
(nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
Cálculo da Média Ponderada = ------------------------------------------------------------------------
soma dos pesos
'''

nota1, peso1, nota2, peso2 = int(input("Digite a primeira nota: ")), int(input("Digite o primeiro peso: ")), int(input("Digite a segundo nota: ")), int(input("Digite o segundo peso: "))

mediaPonderada = ((nota1 * peso1) + (nota2 * peso2))/(peso1+peso2)

print("(({} * {}) + ({} * {})) / ({} + {}) = {}".format(nota1,peso1,nota2,peso2,peso1,peso2,mediaPonderada))
print("Média ponderada = {}".format(mediaPonderada))
