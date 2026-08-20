
# Exercício Prático: Primeira Classe em Python (POO)

# Objetivo: Criar e manipular sua primeira classe em Python, compreendendo na prática como funcionam os atributos, a instanciação de objetos e a execução de métodos.

# Descrição da Atividade:

# Você foi contratado para desenvolver a estrutura inicial de um sistema de cadastro. Para isso, você deve criar uma classe chamada Pessoa seguindo os passos abaixo:

# Definição da Classe e Atributos:

# nome (texto)
# idade (número inteiro)
# cpf (texto)
# email (texto)
# celular (texto)

# Criação dos Métodos:
# cadatrar(self,nome,idade,cpf,email,celular): Método que atribui os valors ao objeto conforme  os 5 dados passados como parâmetros para a pessoa de forma organizada.

# exibir_dados(self): Método que imprime na tela todos os 5 dados cadastrados da pessoa de forma organizada.

# alterar_celular(self, novo_celular): Método que recebe um novo número de telefone como parâmetro e atualiza o atributo celular do objeto.

# Código Principal (Teste prático):


# Crie (instancie) um objeto da classe Pessoa com dados fictícios.
# Chame o método exibir_dados() para mostrar as informações iniciais.
# Chame o método alterar_celular(...) passando um novo número.
# Chame novamente o método exibir_dados() para confirmar se o número do celular foi realmente atualizado.


# Exemplo de Saída Esperada no Console:
# --- DADOS DA PESSOA ---
# Nome: Ana Souza
# Idade: 20
# CPF: 123.456.789-00
# E-mail: ana.souza@email.com
# Celular: (51) 98888-1111

# Número de celular atualizado com sucesso!

# --- DADOS DA PESSOA ---
# Nome: Ana Souza
# Idade: 20
# CPF: 123.456.789-00
# E-mail: ana.souza@email.com
# Celular: (51) 99999-2222


class Pessoa():
    # cadastrar(), mas em vez de ter que instanciar o objeto para então atribuir os valores
    # nós podemos usar um método chamado construct para criar direto com os valores  
    def __init__(self, nome, idade, cpf, email, celular):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.celular = celular

    def exibir_dados(self):
        print("--- DADOS DA PESSOA ---")
        print("Nome: {}".format(self.nome))
        print("Idade: {}".format(self.idade))
        print("CPF: {}.{}.{}-{}".format(self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:]))
        print("E-mail: {}".format(self.email))
        print("Celular: ({}) {}-{}".format(self.celular[:2], self.celular[2:7], self.celular[7:]))
        print("\n")

    def alterar_celular(self, novo_celular):
        self.celular = novo_celular
        print("Número de celular atualizado com sucesso!")
        
# Teste prático
raimundo = Pessoa("raimundo", 40, "00000000000000", "raimundo@gmail.com", "55900000000")
raimundo.exibir_dados()
raimundo.alterar_celular("55911111111")
raimundo.exibir_dados()
