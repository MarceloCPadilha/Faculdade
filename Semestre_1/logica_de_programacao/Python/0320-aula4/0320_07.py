# 7. Ler 3 números e imprimi-los em ordem crescente

vA, vB, vC = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))

lista = [vA, vB, vC]

lista.sort()

for i in lista:
	print(i)
