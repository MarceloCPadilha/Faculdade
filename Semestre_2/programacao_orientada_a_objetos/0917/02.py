class Televisor:
    def __init__(self, modeloTV):
        self.modeloTV = modeloTV # String
        self.canal = 0 # int
        self.volume = 0 # int
        self.estado = 0 # bool: Desligado/Ligado; 0/1

    def exibir_informacoes(self):
        for arg in dir(self):
            # Como o loop em cima vai pegar muito mais do que só as variaveis e os valores a gente filtra
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))

    def botãoPower(self):
        if self.estado is True:
            self.estado = False
        elif self.estado is False:
            self.estado = True

    def definir_volume(self, volume):
        self.volume = volume

    def aumentar_volume(self):
        if self.volume == 100:
            print("Volume já está no máximo.")
        else:
            volume += 1

    def diminuir_volume(self):
        if self.volume == 0:
            print("Volume já está no mínimo.")
        else:
            volume -= 1

    def trocar_canal(self, operando):
        if operando == "+":
            self.canal = (self.canal + 1) % 101
        elif operando == "-":
            self.canal = (self.canal - 1) % 101
        elif isinstance(self.canal, int) and 0 <= canal < 101:
            self.canal = operando
        else:
            print("Canal Inválido")



tv1 = Televisor("Sansumg Smart TV")
tv1.definir_volume(100)
tv1.exibir_informacoes()
print()
tv1.aumentar_volume()
tv1.trocar_canal("-")
tv1.exibir_informacoes()
print()