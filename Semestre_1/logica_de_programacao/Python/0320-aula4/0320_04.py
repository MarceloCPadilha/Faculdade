# 4. Ler três valores numéricos e escrever a média aritmética

vA, vB, vC = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))

def media(*args):
	som = 0
	for i in range(len(args)):
		som += args[i]

	resultado = som / len(args)
	return resultado

print(media(vA, vB, vC))
