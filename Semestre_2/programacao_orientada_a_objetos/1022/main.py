class Animal:
    # Método construtor com seus atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Define método emitir_som que dependerá da espécie do Animal
    def emitir_som(self):
        pass  # Implementar em cada classe filha

    def listar_animal(self):
        print('*' * 25, ' ANIMAL ', '*' * 25)
        print(f'Nome do Pet = {self.nome}')
        print(f'Idade: {self.idade}')
        print('*' * 58, '\n')


# Definição classe FILHA
class Cachorro(Animal):
    # Definição método construtor com atributos da SUPER CLASSE e
    # atributos da classe filha (raca)
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    # Redefinindo o método emitir_som da SUPER CLASSE
    def emitir_som(self):
        print(f'AU AU AU AU')
        print(f"{self.nome} está latindo!")


class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    # Redefinido método emitir_som da SUPER classe
    def emitir_som(self):
        print("Miau Miau Miau Miau")
        print(f"{self.nome} está miando!")

    def listar_animal(self):
        print('*' * 25, ' GATO ', '*' * 25)
        print(f'Nome do Pet = {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'COR: {self.cor}')
        print('*' * 58, '\n')


# Definição classe FILHA
class Passaro(Animal):
    # Definição método construtor com atributos da SUPER CLASSE e
    # atributos da classe filha (especie)
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie

    # Define método específico semelhante ao emitir som, mas somente da classe filha
    def cantar(self):
        print("Piu Piu Piu")
        print(f"{self.nome} está cantando!")

    # Define método da classe filha para listar os dados
    # Chama o método listar_animal da SUPER CLASSE
    # Lista atributos específicos da classe filha
    def listar_passaro(self):
        print('*' * 25, ' PÁSSARO ', '*' * 25)
        self.listar_animal()
        print(f'Espécie : {self.especie}')


# Criando objetos e utilizando métodos construtor de cada OBJETO
cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Frajola", 2, "Frajolinha")
passaro = Passaro("Piu-Piu", 1, "Canario")

# Método redefinido da classe superior com características do OBJETO
cachorro.emitir_som()
gato.emitir_som()

# Método específico do OBJETO
passaro.cantar()

# Método da classe superior, mas não definido na classe filha
passaro.emitir_som()  # Não ocorre erro, desconsidera

gato.listar_animal()
cachorro.listar_animal()

# Método da SUPER CLASSE
passaro.listar_animal()
passaro.listar_passaro()







