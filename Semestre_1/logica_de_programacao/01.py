text = "Olá meu nome é marcelo"

def countVowels(txt):
	vowels = set("aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãõÃÕâêîôûÂÊÎÔÛ")

	count = sum(i in vowels for i in txt)
	return count

print("tem {} vogais".format(countVowels(text)))
