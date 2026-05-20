# Exercício 2:
# Faça um algoritmo que leia o nome de 8 alunos e a quantidade de acertos de uma prova de 10 questões.
# No final diga quantos alunos obtiveram a nota superior a 70% da prova,
# A nota deve ser um inteiro entre 0 e 10. 

mais_de_70 = 0
i = 0

while i < 8:
	total = 10
	print("Qual o nome do aluno? ")
	input()
	questoes = int(input("Quantas questões o aluno acertou? "))
	
	try:
		i += 1
		porcentagem = (questoes / total) * 100

		if porcentagem > 70:
			mais_de_70 += 1
	except ValueError:
		print("Digite algo válido")

print("{} alunos acertaram mais de 70% da prova".format(mais_de_70))
