class Veiculo:
    def __init__(self, marca, modelo, ano, motor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor
        self.velocidade = velocidade


    def listarTudo(self):
        for arg in dir(self):
            # Como o loop em cima vai pegar muito mais do que só as variaveis e os valores a gente filtra
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))

    def listarEspecifico(self, atributo):
        valor = getattr(self, atributo)
        print("{}: {}".format(atributo, valor))

    def updateAtributo(self, atributo):
        valor = input("Digite um novo valor para {}: ".format(atributo))
        # função built in para mudar atributo 
        setattr(self, atributo, valor)
        

    def acelerar(self):
        if self.velocidade >= 150:
            print("Alcançou o limite de velocidade: {}".format(self.velocidade))
        else:
            self.velocidade += 10

    def frear(self):
            if self.velocidade <= 10:
                self.velocidade = 0
                print("O carro parou")
            else:
                self.velocidade -= 10
        

fusca = Veiculo("Wolksvagen", "2 portas", 1970, "Gasolina 1300", 0)

fusca.listarTudo()

fusca.listarTudo()
print()

for i in range(5):
    fusca.acelerar()
    fusca.listarEspecifico("velocidade")

print()

for i in range(5):
    fusca.frear()
    fusca.listarEspecifico("velocidade")

fusca.updateAtributo("motor")
fusca.listarEspecifico("motor")
