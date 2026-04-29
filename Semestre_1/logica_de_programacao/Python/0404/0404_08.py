# Exercício 08.
# Faça um algoritmo para ler o nome de uma pessoa e perguntar se essa pessoa está Feliz. A pessoa deve responder a pergunta com a letra S ou N.
# Mostre também quantas pessoas estão respondendo S e quantas estão respondendo N.

count = 0
feliz = 0
infeliz = 0

while count < 10:	
	for i in range(0, 10):
		nome = str(input("Olá, qual o seu nome? "))
		felicidade = str(input("{} você está feliz? (responda com Y ou N)".format(nome)).lower())
		if felicidade == "y":
			count += 1
			feliz += 1
		elif felicidade == "n":
			count += 1
			infeliz += 1
		else:
			print("ocorreu algum erro")

	print("{} pessoas estão felizes e {} estão infelizes.".format(feliz, infeliz))
