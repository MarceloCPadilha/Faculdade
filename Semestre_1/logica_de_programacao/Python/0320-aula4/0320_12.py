"""
12. Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer
uma viagem até a casa de sua irmã.
Dados extras:
- Distância da casa de Maria até sua irmã : 520 km
- Seu carro consome 12 Km/litro de combustível.
- Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.
Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de
combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a
viagem e o custo da viagem.
"""

dist, consu, valorporlitro = float(input("Digite a distância até o destino: ")), float(input("Digite o consumo de gasolina por kilometro: ")), float(input("Digite o valor da gasolina em reais por litro: "))

def getCustoDaViagem(distancia, consumo, valorPorLitro):
	custo = distancia / consumo * valorPorLitro
	return custo

def getConsumoDeCombustivel(distanc, consum):
	consumoTotal = distanc / consum
	return consumoTotal

print("A viagem gastará {} litros de gasolina e custará R${}.".format(getConsumoDeCombustivel(dist, consu), getCustoDaViagem(dist, consu, valorporlitro)))
