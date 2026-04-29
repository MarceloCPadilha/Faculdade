# Exercício 09.
# Faça um algoritmo para imprimir a seguinte figura:
# 1
# 12
# 123
# 1234
# 12345

lenght = input("linhas? ")

# for i in range(1, lenght):
# 	for j in range(1, i + 1):
# 		print(j, end="")
# 	print()

linha = ""
for i in range(1, lenght):
	linha = linha + str(i)
	print(linha)