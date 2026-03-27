# 6. Fazer um algoritmo para ler dois números e mostrar o maior deles.

vA, vB = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))

# if vA > vB:
# 	print("O primeiro número é maior que o segundo")
# elif vB > vA:
# 	print("O segundo número é maior que o primeiro")
# else:
# 	print("Os dois números são iguais")

def getGreater(*args):
	atualMaior = args[0]
	for i in range(len(args)):
		if args[i] > atualMaior:
			atualMaior = args[i]

	return atualMaior

print(getGreater(vA, vB))
