# Objetivo: Praticar a criação de classes em Python, uso do construtor __init__, atributos de
# instância e métodos com validação condicional.

# Contexto:
# Você foi encarregado de desenvolver o módulo de controle de camisas para o sistema de uma
# loja de roupas. O sistema deve permitir o cadastro de novas peças, a visualização dos dados e
# o registro de vendas com baixa no estoque.

# Requisitos:
# 1. Crie a classe Camisa.

# 2. No método construtor __init__, defina e inicialize os seguintes atributos:

# - cor (texto)
# - tamanho (texto: "P", "M", "G", "GG")
# - preco (número decimal)
# - tipo_gola (texto: ex: "Gola Polo", "Gola V", "Gola Redonda")
# - quantidade_estoque (número inteiro)

# 3. Implemente os seguintes métodos na classe:
# - exibir_informacoes(): Mostra na tela todos os dados da camisa de forma organizada.
# - vender(quantidade): Recebe a quantidade de peças a serem vendidas. Se houver
# estoque suficiente, realiza a subtração e exibe o estoque restante; caso contrário, exibe
# uma mensagem avisando que o estoque é insuficiente.

# 4. Área de Teste:
# - Crie um objeto da classe Camisa (ex: cor "Azul", tamanho "M", preço 79.90, gola "Polo",
# estoque 10).
# - Chame o método exibir_informacoes().
# - Realize uma venda válida (ex: 3 unidades).
# - Tente realizar uma venda com quantidade maior do que o estoque disponível para testar
# a validação.

class Camisa:
    def __init__(self, cor, tamanho, preco, tipo_gola, quantidade_estoque):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.tipo_gola = tipo_gola
        self.quantidade_estoque = quantidade_estoque

    def exibir_informacoes(self):
        for arg in dir(self):
            # Como o loop em cima vai pegar muito mais do que só as variaveis e os valores a gente filtra
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))

    def vender(self, quantidade):
        if self.quantidade_estoque < quantidade:
            print("Não foi possivel realizar a compra. Estoque insuficiente.")
        else:
            self.quantidade_estoque -= quantidade
            print("Compra realizada com sucesso. Estoque restante {}".format(self.quantidade_estoque))



camisa_gremio_oficial = Camisa("Azul, preto e branco", "G", 700.00, "Gola normal", 50)

camisa_gremio_oficial.exibir_informacoes()

print()
camisa_gremio_oficial.vender(51)

print()
camisa_gremio_oficial.vender(50)

print()
