class Tutor:
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

    def exibir_dados(self):
        print("*" * 20, "Tutor", "*" * 20)
        for arg in dir(self):
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))
        print("*" * 47)


class Pet:
    def __init__(self, nome: str, especie: str, tutor: Tutor):
        self.nome = nome
        self.especie = especie
        self.tutor = tutor
        
    def exibir_dados(self):
        print("*" * 20, "Pet", "*" * 20)
        for arg in dir(self):
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))
        self.tutor.exibir_dados()


tutor1 = Tutor("Marcelo", "999999999")

pet1 = Pet("Mimi", "Gato", tutor1)
pet2 = Pet("Branquinha", "Gato", tutor1)
pet3 = Pet("Cookie", "Cachorro", tutor1)

pet1.exibir_dados()