class Veiculo:
    def __init__(self, marca, modelo, ano, preco_diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco_diaria = preco_diaria

    def calcular_aluguel(self, dias):
        """Calcula o valor total do aluguel."""
        return self.preco_diaria * dias

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, numero_portas):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.numero_portas = numero_portas

    def calcular_aluguel(self, dias):
        """Calcula o valor do aluguel para carro com desconto para longos períodos."""
        valor_base = super().calcular_aluguel(dias)
        if dias > 7:
            # Aplica um desconto de 10%
            desconto = 0.10 * valor_base
            return valor_base - desconto
        return valor_base
        
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, cilindrada):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.cilindrada = cilindrada

    def calcular_aluguel(self, dias):
        """Calcula o valor do aluguel para moto com taxa adicional de seguro."""
        valor_base = super().calcular_aluguel(dias)
        # Aplica uma taxa adicional de 5%
        taxa_seguro = 0.05 * valor_base
        return valor_base + taxa_seguro

# Exemplo de Uso:
# Criação de um carro
carro = Carro(marca="Toyota", modelo="Corolla", ano=2020, preco_diaria=150.0, numero_portas=4)
valor_aluguel_carro_curto = carro.calcular_aluguel(dias=5)
print(f"Valor do aluguel do carro por 5 dias: R${valor_aluguel_carro_curto:.2f}")

valor_aluguel_carro_longo = carro.calcular_aluguel(dias=10)
print(f"Valor do aluguel do carro por 10 dias: R${valor_aluguel_carro_longo:.2f}")

# Criação de uma moto
moto = Moto(marca="Honda", modelo="CB500", ano=2019, preco_diaria=100.0, cilindrada=500)
valor_aluguel_moto = moto.calcular_aluguel(dias=5)
print(f"Valor do aluguel da moto por 5 dias: R${valor_aluguel_moto:.2f}")
