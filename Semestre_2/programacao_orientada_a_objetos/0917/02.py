class Televisor:
    def __init__(self, modeloTV):
        self.modeloTV = modeloTV # String
        self.canal = 0 # int
        self.volume = 0 # int
        self.estado = 0 # bool: Desligado/Ligado; 0/1


    def botãoPower(self):
        if self.estado is True:
            self.estado = False
        elif self.estado is False:
            self.estado = True

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

    def trocar_canal(self, canal):
        if canal == "+":
            self.canal = (canal + 1) % 101
        elif canal == "-":
            self.canal = (canal - 1) * 101
        elif isinstance(canal, int) and 0 <= canal < 101:
            self.canal = canal
        else:
            print("Canal Inválido")



tv1 = Televisor("Sansumg Smart TV")