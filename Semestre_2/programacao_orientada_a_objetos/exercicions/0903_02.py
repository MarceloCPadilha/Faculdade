# Seguindo o modelo que você forneceu, aqui está um novo exercício focado no assunto Produto, mantendo a estrutura de Programação Orientada a Objetos em Python:

# Exercício de Programação Orientada a Objetos: Classe Produto
# Enunciado:

# Crie uma classe chamada Produto que represente um item no inventário de uma loja. A classe deve possuir os seguintes atributos:

# codigoProduto (inteiro): O identificador único do produto.
# nomeProduto (string): O nome ou descrição do produto.
# preco (float): O valor unitário do produto.
# quantidadeEstoque (inteiro): A quantidade disponível em estoque.
# A classe deve implementar os seguintes métodos:

# Construtor (__init__):
# Deve receber o código, nome, preço e quantidade inicial.
# Deve inicializar os atributos da classe.
# exibirDetalhes():
# Deve imprimir as informações do produto no formato:
# "ID: [codigoProduto] | Produto: [nomeProduto] | Preço: R$ [preco] | Estoque: [quantidadeEstoque]"
# atualizarPreco(novo_preco):
# Deve receber o novo valor e atualizar o atributo preco.
# vender(quantidade):
# Deve receber a quantidade a ser vendida.
# Se houver estoque suficiente, subtrair a quantidade do atributo quantidadeEstoque.
# Caso contrário, exibir uma mensagem de "Estoque insuficiente".
# Exemplo de uso esperado:

# Python

# # Exemplo de uso da classe Produtoprod1 = Produto(501, "Teclado Mecânico", 150.00, 20)prod1.exibirDetalhes()  # Saída: ID: 501 | Produto: Teclado Mecânico | Preço: R$ 150.0 | Estoque: 20prod1.atualizarPreco(135.50)prod1.vender(5)prod1.exibirDetalhes()  # Saída: ID: 501 | Produto: Teclado Mecânico | Preço: R$ 135.5 | Estoque: 15
# Instruções adicionais:

# Validação: No construtor, garanta que o preco e a quantidadeEstoque não sejam valores negativos.
# Desafio Extra: Adicione um método chamado reporEstoque(quantidade) que soma o valor recebido ao estoque atual.
# Teste: Instancie pelo menos três produtos diferentes (ex: Mouse, Monitor, Headset) para validar o comportamento da classe.

class Produto:
    def __init__(self, codigoProduto, nomeProduto, preco, quantidadeEstoque):
        error = []
        if not isinstance(codigoProduto, int):
            error.append("O código do produto deve ser um número inteiro")
        if not isinstance(nomeProduto, str):
            error.append("O nome do produto deve ser uma string")
        if not isinstance(preco, float):
            error.append("O preço deve ser do tipo float")
        if not isinstance(quantidadeEstoque, int):
            error.append("O estoque deve ser um número inteiro")
        if quantidadeEstoque < 0:
            error.append("O estoque deve ser zero ou um número positivo")

        if not error:
            self.codigoProduto = codigoProduto
            self.nomeProduto = nomeProduto
            self.preco = preco
            self.quantidadeEstoque = quantidadeEstoque
        else:
            for i in error:
                print(i, "\n")

    def exibirDetalhes(self):
        for arg in dir(self):
            if not arg.startswith('__') and not callable(getattr(self, arg := arg)):
                valor = getattr(self, arg)
                print("{}: {}".format(arg, valor))

    def atualizarPreco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
        else:
            print("Preço inválido")

    def vender(self, quantidade):
        if self.quantidadeEstoque < quantidade:
            print("Não foi possivel realizar a venda. Estoque insuficiente.")
        else:
            self.quantidadeEstoque -= quantidade
            print("Venda realizada com sucesso. Estoque restante {}".format(self.quantidadeEstoque))


prod1 = Produto(501, "Teclado Mecânico", 150.00, 20)
prod1.exibirDetalhes()  # Saída: ID: 501 | Produto: Teclado Mecânico | Preço: R$ 150.0 | Estoque: 20
prod1.atualizarPreco(135.50)
prod1.vender(5)
prod1.exibirDetalhes()  # Saída: ID: 501 | Produto: Teclado Mecânico | Preço: R$ 135.5 | Estoque: 15