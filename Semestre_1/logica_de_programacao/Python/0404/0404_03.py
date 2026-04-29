# Exercício 03.
# Faça um algoritmo que leia uma frase digitada pelo usuário e imprima essa frase na tela.
# Imprima também a quantidade de caracteres digitados e q quantidades de letras ' a ' existentes.

frase = input("Digite uma frase:\n")

for i in range(len(frase)):
	a = set("aAáÁàÀãÃâÂ")
	count = sum(i in a for i in frase)

print("a frase é:\n{}".format(frase))
print("A frase contém {} caracteres.\n" 
	"A frase contém {} caracteres 'a'.".format(len(frase), count))
