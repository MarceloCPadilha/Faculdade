# 7. Ler 3 números e imprimi-los em ordem crescente

vA, vB, vC = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))

lista = [vA, vB, vC]

# não aprende nada, trapaça
# lista.sort()

# print(lista)


# forma 1
def bubblesort(lista):
	rang = len(lista)
	for i in range(rang):
		# se ele passar pela condicional do segundo loop não da trigger no break 
		# o que significa que a lista não está ordenada ainda
		# se ele não passar pela condicional do segundo loop a lista está ordenada, pois não precisa mais trocar
		trocou = False
		for j in range(0, rang - i - 1):
			# só para se não estiver ordenado
			if lista[j+1] < lista[j]:
				lista[j+1], lista[j] = lista[j], lista[j+1]
				# se entrou nesse loop trocou vira falso senão continua no break
				trocou = True
		if trocou == False:
			break
	return lista

print(bubblesort(lista))

# forma 2
# def quicksort():



