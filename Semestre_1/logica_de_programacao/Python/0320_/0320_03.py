# 3. Ler dois valores numéricos e escrever a soma destes

vA, vB = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))

def soma(*args):
	soma = 0
	for i in range(len(args)):
		soma += args[i]

	return soma

print(soma(vA, vB))
