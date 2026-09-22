# Objetivo: Praticar o uso de atributos booleanos (Verdadeiro/Falso), instanciação de objetos e
# métodos para atualização e reposição de estoque.

# Contexto:
# Com a chegada do inverno, a loja começou a receber lotes de blusões. O sistema precisa
# registrar as características da peça (incluindo se possui capuz) e gerenciar as reposições
# periódicas de estoque.

# Requisitos:
# 1. Crie a classe Blusao.

# 2. No método construtor __init__, defina e inicialize os seguintes atributos:
# - cor (texto)
# - tamanho (texto: "P", "M", "G", "GG")
# - preco (número decimal)
# - possui_capuz (booleano: True ou False)
# - quantidade_estoque (número inteiro)

# 3. Implemente os seguintes métodos na classe:
# - exibir_informacoes(): Mostra os detalhes do blusão, indicando textualmente se a peça
# possui capuz ou não, junto com preço e estoque.
# - repor_estoque(quantidade): Recebe uma quantidade de peças que chegaram do
# fornecedor, soma ao estoque atual e mostra o total atualizado.

# 4. Área de Teste:
# - Crie um objeto da classe Blusao (ex: cor "Cinza", tamanho "G", preço 180.00,
# possui_capuz True, estoque 4).
# - Chame o método exibir_informacoes().
# - Realize uma reposição de 6 peças utilizando o método repor_estoque(6).
# - Chame exibir_informacoes() novamente para verificar o estoque final.

class Calca:
    def __init__(self, cor, tamanho, preco, possui_capuz, quantidade_estoque):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.possui_capuz = possui_capuz
        self.quantidade_estoque = quantidade_estoque

    def exibir_informacoes(self):
        for arg in dir(self):
            # Como o loop em cima vai pegar muito mais do que só as variaveis e os valores a gente filtra
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))

    def repor_estoque(self, quantidade):
        self.quantidade_estoque += quantidade


blusao = Calca("Cinza", "G", 180.00, True, 4)

blusao.exibir_informacoes()
print()

blusao.repor_estoque(6)
print()

blusao.exibir_informacoes()
print()
