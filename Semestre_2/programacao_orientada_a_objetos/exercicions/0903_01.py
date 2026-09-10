# Exercício
# Exercício de Programação Orientada a Objetos em Python, focado na criação de uma classe `Departamento`:

# **Enunciado:**
# Crie uma classe chamada `Departamento` que represente um departamento de uma empresa. A classe deve ter os seguintes atributos:
# * `codigoDepartamento` (inteiro): O código único do departamento.
# * `nomeDepartamento` (string): O nome do departamento.
# * `nomeGerente` (string): O nome do gerente responsável pelo departamento.
# A classe deve implementar os seguintes métodos:

# 1. **Construtor (`__init__`)**:
#   * Deve receber como parâmetros o código do departamento, o nome do departamento e o nome do gerente.
#   * Deve inicializar os atributos da classe com os valores recebidos.

# 2. **`listarDepartamento()`**:
#   * Deve imprimir na tela as informações do departamento no seguinte formato:
#     * "Código: [codigoDepartamento], Nome: [nomeDepartamento], Gerente: [nomeGerente]"

# 3. **`mudarGerente(novo_gerente)`**:
#   * Deve receber como parâmetro o novo nome do gerente.
#   * Deve atualizar o atributo `nomeGerente` com o novo nome.

# **Exemplo de uso:**
# python
# # Exemplo de uso da classe Departamento
# departamento1 = Departamento(101, "Recursos Humanos", "Ana Silva")
# departamento1.listarDepartamento() # Saída: Código: 101, Nome: Recursos Humanos, Gerente: Ana Silva
# departamento1.mudarGerente("Carlos Oliveira")
# departamento1.listarDepartamento() # Saída: Código: 101, Nome: Recursos Humanos, Gerente: Carlos Oliveira

# **Instruções adicionais:**
# * Implementar a classe `Departamento` completa, incluindo o construtor e os métodos especificados.
# * Adicionar validações básicas, como verificar se o código do departamento é um número inteiro.
# * Como um desafio extra, adicionar um método para mudar o nome do departamento ou incluir outros atributos relevantes.
# * Criar outros objetos do tipo departamento, para testar a classe criada.

class Departamento:
    def __init__(self, codigoDepartamento, nomeDepartamento, nomeGerente):
        if not isinstance(codigoDepartamento, int):
            raise TypeError("O código do departamento deve ser um número inteiro.")
        self.codigoDepartamento = codigoDepartamento
        self.nomeDepartamento = nomeDepartamento
        self.nomeGerente = nomeGerente

    def listarDepartamento(self):
        for arg in dir(self):
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))

    def mudarGerente(self, novo_gerente):
        novo_gerente = input("Digite o nome do novo gerente: ")
        self.nome_gerente = novo_gerente

departamento1 = Departamento(101, "Recursos Humanos", "Ana Silva")
departamento1.listarDepartamento() # Saída: Código: 101, Nome: Recursos Humanos, Gerente: Ana Silva
departamento1.mudarGerente("Carlos Oliveira")
departamento1.listarDepartamento() # Saída: Código: 101, Nome: Recursos Humanos, Gerente: Carlos Oliveira