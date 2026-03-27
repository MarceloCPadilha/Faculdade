# 6. Fazer um algoritmo para ler dois números e mostrar o maior deles.

vA, vB = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))

def getGreater(*args):
	atualMaior = args[0]
	for i in range(len(args)):
		if args[i] > args[i - 1]:
			atualMaior = args[i]

	return atualMaior

print(getGreater(vA, vB))
