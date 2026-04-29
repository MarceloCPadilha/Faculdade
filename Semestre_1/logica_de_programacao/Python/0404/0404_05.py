# Exercício 05.
# Faça um algoritmo que leia um número inteiro e imprima a mensagem:
# - "Número está no intervalo entre correto."  (Quando o número digitado estiver no intervalo entre 20 e 50).

numero = 40
if numero < 20:
	print("O número está fora do intervalo requisitado")
elif numero >= 20 and numero <= 50:
	print("O número está dentro do intervalo requisitado")
else:
	print("O número está fora do intervalo requisitado")