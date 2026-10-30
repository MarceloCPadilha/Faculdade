class Consulta:
    def __init__(self, data: str, hora: str):
        self.data = data
        self.hora = hora

    def exibir_consulta(self):
        return "Data: {} | Hora: {}".format(self.data, self.hora)

class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = []

    def emitir_som(self):
        pass

    def agendar_consulta(self, data: str, hora: str):
        consulta = Consulta(data, hora)
        self.historico_consultas.append(consulta)

    def listar_consultas(self):
        print("Consultas de {}:".format(self.nome))
        if not self.historico_consultas:
            print("Nenhuma consulta agendada.")
            return
        for i, consulta in enumerate(self.historico_consultas, start=1):
            print("  {}. {}".format(i, consulta.exibir_consulta()))

    def listar_animal(self):
        print("-" * 35)
        print("Nome do Pet: {} | Idade: {} anos".format(self.nome, self.idade))
        print("-" * 35)

class Cachorro(Animal):
    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print("{} diz: Au-au, awoooo!".format(self.nome))

class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor: str):
        super().__init__(nome, idade)
        self.cor = cor

    def emitir_som(self):
        print("{} diz: Meow, purr purr".format(self.nome))

    def listar_animal(self):
        print("-" * 35)
        print("Nome do Pet: {} | Idade: {} anos | Cor do pelo: {}".format(self.nome, self.idade, self.cor))
        print("-" * 35)

class Passaro(Animal):
    def __init__(self, nome: str, idade: int, especie: str):
        super().__init__(nome, idade)
        self.especie = especie

    def cantar(self):  
        print("{} canta: Piu Piu!".format(self.nome))

    def listar_passaro(self):
        self.listar_animal() 
        print("Espécie: {}".format(self.especie))

cachorro1 = Cachorro("cachorro1", 1, "Labrador")
Gato1 = Gato("Gato1", 1, "Siamês")
Passaro1 = Passaro("Passaro1", 1, "Papagaio")

print()
print(" Som:")
cachorro1.emitir_som()
Gato1.emitir_som() 
Passaro1.cantar()

cachorro1.agendar_consulta("01/11/2026", "14:40")
cachorro1.agendar_consulta("02/11/2026", "19:50")
Gato1.agendar_consulta("02/11/2026", "8:35")

print()
print("Cadastros:")
cachorro1.listar_animal()
Gato1.listar_animal()
Passaro1.listar_passaro()

print()
print("Históricos:")
cachorro1.listar_consultas()
Gato1.listar_consultas()
Passaro1.listar_consultas()
