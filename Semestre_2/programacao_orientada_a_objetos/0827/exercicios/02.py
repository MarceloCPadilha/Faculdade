# Objetivo: Praticar a definição de classes, manipulação de valores numéricos em atributos e
# aplicação de cálculos por meio de métodos.

# Contexto:
# A loja de roupas precisa controlar o estoque de calças e aplicar remarcações de preço
# promocionais em peças paradas no estoque.

# Requisitos:
# 1. Crie a classe Calca.

# 2. No método construtor __init__, defina e inicialize os seguintes atributos:
# - cor (texto)
# - tamanho (número inteiro: ex: 38, 40, 42)
# - preco (número decimal)
# - tipo_tecido (texto: ex: "Jeans", "Sarja", "Moletom")
# - quantidade_estoque (número inteiro)

# 3. Implemente os seguintes métodos na classe:
# - exibir_informacoes(): Exibe os detalhes da calça formatados na tela.
# - aplicar_desconto(porcentagem): Recebe um valor de porcentagem (ex: 10 para 10%),
# calcula o desconto, atualiza o atributo preco da peça com o novo valor reduzido e exibe
# uma mensagem com o novo preço.

# 4. Área de Teste:
# - Crie um objeto da classe Calca (ex: cor "Preta", tamanho 42, preço 120.00, tecido
# "Jeans", estoque 8).
# - Chame o método exibir_informacoes().
# - Aplique um desconto de 15% utilizando aplicar_desconto(15).
# - Chame exibir_informacoes() novamente para confirmar a alteração permanente do
# preço.

class Calca:
    def __init__(self, cor, tamanho, preco, tipo_tecido, quantidade_estoque):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.tipo_gola = tipo_tecido
        self.quantidade_estoque = quantidade_estoque

    def exibir_informacoes(self):
        for arg in dir(self):
            # Como o loop em cima vai pegar muito mais do que só as variaveis e os valores a gente filtra
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))

    def aplicar_desconto(self, desconto_numero_inteiro_para_porcentagem):
        self.preco -= self.preco * (desconto_numero_inteiro_para_porcentagem / 100)

calca = Calca("Preta", "42", 120.00, "Jeans", 8)

calca.exibir_informacoes()
print()

calca.aplicar_desconto(10)
print()

calca.exibir_informacoes()
print()
