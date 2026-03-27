text = input("Digite um texto: ")

def countVowels(args):
	# aqui se usa o set, pois ele tem tempo de busca constante O(1) por ser um hashmap
	# set constructor, pois apesar de ser mais lento que o normal é mais conveniente para escrever
	# exmplo x = {"olaa"} -> { "olaa" } enquanto x = set("olaa") -> { "o", "l", "a"}
	vowels = set("aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãõÃÕâêîôûÂÊÎÔÛ") 

	# list comprehension, pois evita escrever muitos IFs
	count = sum(i in vowels for i in args)
	return count

print("O texto tem {} vogais".format(countVowels(text)))
print("As vogais compõe {:2}% do texto".format(countVowels(text) * 100 / len(text.replace(" ", ""))))
print("")
 