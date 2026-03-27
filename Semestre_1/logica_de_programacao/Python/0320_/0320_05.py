# 5. Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média.

vA, vB, vC, vD, vE= int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: ")), int(input("Digite o quarto número: ")), int(input("Digite o quinto número: "))

def soma(*args):
	soma = 0
	for i in range(len(args)):
		soma += args[i]

	return soma

def media(*args):
	som = 0
	for i in range(len(args)):
		som += args[i]

	resultado = som / len(args)
	return resultado

print("A soma é {} e a média aritmetica é {}".format(soma(vA, vB, vC, vD, vE), media(vA, vB, vC, vD, vE)))
