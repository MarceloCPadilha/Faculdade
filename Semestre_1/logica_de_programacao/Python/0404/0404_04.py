# Exercício 04.
# Faça um algoritmo que leia o nome e a idade de uma pessoa e imprima a mensagem :
# - "Você é jovem" se a pessoa tiver menos de 18 anos.
# - "Você é um adulto" Se a pessoa tiver a idade entre 18 e 60 anos.
# - "Você é um idoso" Se a pessoa tiver mais que 60 anos.

idade = int(input("Digite sua idade: "))

if idade < 0:
	print("entre uma idade válida")
elif idade < 18:
	print("Jovem")
elif idade > 17 and idade < 61:
	print("Adulto")
elif idade > 60:
	print("Idoso")