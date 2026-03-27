'''
11. Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
Centígrados.
(Fahrenheit – 32) x 5
Fórmula: Centígrados = ----------------------------
9
'''

tempFahr = float(input("Digite uma temperatura em fahrenheit: "))

def convertToCelcius(tempFahr):
	tempCelc = ((tempFahr	- 32) * 5) / 9
	return tempCelc

print(convertToCelcius(tempFahr))
