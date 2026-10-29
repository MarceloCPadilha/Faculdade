

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)  # Chama o construtor da superclasse
        self.cargo = cargo

    def apresentar(self):
        return f"{super().apresentar()} Eu sou um {self.cargo}."


# Passo 3: Definindo a Classe Professor (Composição)

class Professor:
    def __init__(self, nome, idade, disciplina):
        self.funcionario = Funcionario(nome, idade, "Professor")
        self.disciplina = disciplina

    def apresentar(self):
        return f"{self.funcionario.apresentar()} Eu ensino a disciplina de {self.disciplina}."


# Passo 4: Usando as Classes

#Agora, vamos criar instâncias das classes e ver como tudo funciona.


# Criando uma instância de Funcionario
funcionario = Funcionario("Carlos", 30, "Analista")
print(funcionario.apresentar())  # Saída: Olá, meu nome é Carlos e tenho 30 anos. Eu sou um Analista.

# Criando uma instância de Professor
professor = Professor("Ana", 35, "Matemática")
print(professor.apresentar())  # Saída: Olá, meu nome é Ana e tenho 35 anos. Eu sou um Professor. Eu ensino a disciplina de Matemática.

prof2 = Funcionario("Vera", 25,"Professor")
# prof2 é OBJETO Funcionário JAMAIS terá disciplina

print(prof2.apresentar())
prof2.disciplina='POO'
# prof2 não consegue atribuir disciplina nem listar pois não é da CLASSE Professor
print(prof2.apresentar())
print('XXXX')
# Para ter disciplina tem que ser da classe Professor
prof2 = Professor("Vera",25,'Química')
print(prof2.apresentar())
