"""
Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3, conforme a condição:
se n <= 10 imprima MENSAGEM 1,
se n > 10 e <= 100 imprima MENSAGEM 2
se n >100 imprima MENSAGEM 3
"""

# desculpa não ter mensagem, não tinha tempo pra pensar
n = int(input("Digite um número: "))

if n <= 10:
	print("MENSAGEM 1")
elif n > 10 and n <= 100:
	print("MENSAGEM 2")
elif n > 100:
	print("MENSAGEM 3")
