# xercício 11.
# Faça um algoritmo para imprimir a seguinte figura:
# #1#3#5#7#9
# 0#2#4#6#8#
# #1#3#5#7#9
# 0#2#4#6#8#
# #1#3#5#7#9
# 0#2#4#6#8#

for i in range(6):
	if i % 2 == 0:
		for j in range(0, 9, 2):
			print(j, end="#")
		print()
	elif i % 2 != 0:
		for j in range(1, 10, 2):
			print("#{}".format(j), end="")
		print()

# for linha in range(6):
# 	for coluna in range(10):
# 		if linha % 2 == 0 and coluna % 2 == 0:
# 			print("#", end="")
# 		if linha % 2 != 0 and coluna % 2 != 0:
# 			print("", end="#")
# 		else:
# 			print(coluna, end="")
# 	print()
