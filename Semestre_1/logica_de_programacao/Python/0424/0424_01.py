# Faça um algoritmo que leia uma string no formato de data (dd/mm/aaaa)
# e escreva esta com o nome do mês por extenso.
# Exemplo:
# entrada: 25/04/2025
# saida : 25 de abril de 2025.

data = input("Digite a data (formato: dd/mm/aaaa): ")

dia, mes, ano = data.split("/")

if int(dia) < 1 or int(dia) > 31:
	print("Dia inválido")

if int(mes) < 1 or int(mes) > 12:
	print("Mês inválido")

if int(mes) > 0 and int(mes) < 13 and int(dia) > 0 and int(dia) < 32:
	meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
		"julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

	print("{} de {} de {}".format(dia, meses[int(mes)], ano))
