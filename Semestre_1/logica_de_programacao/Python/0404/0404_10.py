# Exercício 10.
# Faça um algoritmo para imprimir a seguinte figura:
# #
# ##
# #2#
# #23#
# #234#
# #2345#
# #23456#
# #234567#
# #2345678#
# #########

lenght = 8
for i in range(0, lenght + 2):
	if i == 0:
		print("#")
	elif i == 1:
		print("##")
	elif i < lenght + 1:
		print("#", end="")
		for j in range(2, i + 1):
			print(j, end="")
		print("#")
	else:
		print("#" * i)

# linha = ""
# for coluna in range(0, 9):
# 	if coluna > 1:
# 		linha += str(coluna)
# 	print(linha + "#")
# 	if coluna == 0:
# 		linha = "#"
# print("#"*(coluna+1))

