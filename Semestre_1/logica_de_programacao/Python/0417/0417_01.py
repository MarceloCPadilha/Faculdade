# Faça um algoritmo que leia o nome e a altura de várias pessoas.
# No final, mostre o nome e a altura das pessoas mais altas e
# das mais baixas. Informe também a altura média.

lista = [
		{"nome": "aaa", "altura": 150},
		{"nome": "bbb", "altura": 160},
		{"nome": "ccc", "altura": 170},
		{"nome": "ddd", "altura": 180}
		]

while True:	
	mais = input("Queres adicionar pessoas (y/n)? ")

	if mais == "y":
		try: 
			novo_nome = input("Digite o nome: ")
			nova_altura = int(input("Digite a altura em cm(ex: 180): "))

			nova_pessoa = {"nome": novo_nome, "altura": nova_altura}
			lista.append(nova_pessoa)
		except:
			print("ocorreu algum erro")
			continue
	elif mais == "n":
		break

	for i in lista:
		print("Nome: {}, altura: {}".format({i['nome']}, {i['altura']}))

maior = lista[0]["altura"]
menor = lista[0]["altura"]
soma = 0

for i in lista:
	soma += i["altura"]

	if i["altura"] < menor:
		menor = i["altura"]

	if i["altura"] > maior:
		maior = i["altura"] 

media = soma / len(lista)

print("pessoa mais alta: {}\npessoa mais baixa: {}\nmédia das alturas: {}".format(maior, menor, media))