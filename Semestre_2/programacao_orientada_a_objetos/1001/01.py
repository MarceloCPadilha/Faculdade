# Enunciado do Exercício:
# Crie um sistema simples de gerenciamento de uma transportadora utilizando programação orientada a objetos em Python.

# Requisitos:

# Classe Caminhão:
# Atributos: modelo, placa, capacidade_carga.
# Métodos: carregar(peso), descarregar(peso). O método carregar deve verificar se o peso a ser carregado não excede a capacidade do caminhão.
# Classe Motorista:
# Atributos: nome, idade, CNH. dataValidade
# Métodos: dirigir(caminhao). Este método deve imprimir uma mensagem indicando que o motorista está dirigindo o caminhão.
# verificarValidade(motorista)
# Associação entre as classes:
# Um caminhão deve ser dirigido por apenas um motorista.
# Um motorista pode dirigir vários caminhões.
# Exercícios:

# Crie pelo menos 3 objetos da classe Caminhão e 2 objetos da classe Motorista.
# Atribua um motorista a cada caminhão.
# Simule a carga e descarga de um caminhão.
# verifique se a CNH do Motorista é stá valida, caso estiver para vencer em 30 dias ou vencida verificar se o motorista está associado a um caminhão e avisar para renovar a CNH
# Imprima na tela informações sobre os caminhões e seus respectivos motoristas.
# Dicas:

# Utilize a associação entre as classes para conectar um objeto caminhão a um objeto motorista.
# Explore os métodos de cada classe para simular as ações da transportadora.
# Utilize a orientação a objetos para modelar o problema de forma clara e organizada.
# Exemplo de saída:

# Caminhão:Modelo: Mercedes BenzPlaca: AAA-1234Capacidade de carga: 10000 kgMotorista: João SilvaCarga atual: 5000 kgCaminhão:...
# Desafios:

# Adicione um atributo "carga_atual" à classe Caminhão para controlar o peso carregado.
# Implemente um método para calcular o frete de um transporte com base na distância e no peso da carga.
# Crie uma classe "Viagem" para armazenar informações sobre as viagens realizadas pelos caminhões.
# Este exercício tem como objetivo:

# Fortalecer a compreensão sobre a associação entre classes em Python.
# Aplicar os conceitos de programação orientada a objetos em um cenário real.
# Desenvolver a lógica de programação e a capacidade de resolver problemas.
# Bons estudos!

# Observações:

# Este enunciado pode ser adaptado para níveis de complexidade diferentes, adicionando mais classes, atributos e métodos.
# Incentive os alunos a utilizarem boas práticas de programação, como nomes de variáveis e funções significativos, comentários e formatação do código.
# Possíveis extensões:

# Adicionar uma classe "Cliente" para representar os clientes da transportadora.
# Implementar um sistema de login para os motoristas.
# Criar um relatório com as informações de todos os caminhões e motoristas.
# Com este exercício, os alunos poderão explorar os conceitos de orientação a objetos de forma prática e divertida, aplicando seus conhecimentos para criar um sistema simples, mas funcional.


RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"
AMARELO="\033[33m"



from datetime import datetime, timedelta
from stringprep import map_table_b2


class Motorista:
    def __init__(self, nome: str, idade: int, CNH: str, dataValidade: str):
        self.nome = nome
        self.idade = idade
        self.CNH = CNH
        # Converte a string no formato DD/MM/AAAA para um objeto datetime
        self.dataValidade = datetime.strptime(dataValidade, "%d/%m/%Y")




    def verificarValidade(self):
        hoje = datetime.now()
        dias_para_vencer = (self.dataValidade - hoje).days

        if dias_para_vencer < 0:
            print(f"{RED}ALERTA: A CNH do motorista {self.nome} está VENCIDA! {self.dataValidade}{RESET}")
            return False
        elif dias_para_vencer <= 30:
            print(f"{AMARELO} ATENÇÃO: A CNH do motorista {self.nome} vence em {dias_para_vencer} dias {self.dataValidade} . É necessário renovar!{RESET}")
            return True
        else:
            print(f"{GREEN} CNH do motorista {self.nome} está válida.{RESET}")
            return True


class Caminhão:
    def __init__(self, modelo: str, placa: str, capacidade_carga: float, motorista: Motorista = None):
        self.modelo = modelo
        self.placa = placa
        self.capacidade_carga = capacidade_carga
        self.carga_atual = 0.0  # Atributo do Desafio
        self.motorista = motorista

    def motorista_responsavel(self,motorista):
        if self.motorista is None:
            self.motorista=motorista
            print(f'Motorista associado {self.motorista.nome} com sucesso ao caminhão {self.placa}')
        else:
            print(f'Motorista Atual: {self.motorista.nome}')
            self.motorista = motorista
            print(f'Trocado por {self.motorista.nome} com sucesso com sucesso ao caminhão {self.placa}')


    def carregar(self, peso: float):
        if self.carga_atual + peso <= self.capacidade_carga:
            self.carga_atual += peso
            print(f"Carga de {peso} kg adicionada com sucesso ao caminhão {self.placa}. Carga atual: {self.carga_atual} kg.")
        else:
            capacidade_disponivel = self.capacidade_carga - self.carga_atual
            print(f"❌{RED}{BOLD} Não é possível carregar {AMARELO}{peso}{RED} kg no caminhão {self.placa}. Excede a capacidade! (Disponível: {capacidade_disponivel} kg){RESET}")

    def descarregar(self, peso: float):
        if peso <= self.carga_atual:
            self.carga_atual -= peso
            print(f"Descarregado {peso} kg do caminhão {self.placa}. Carga atual: {self.carga_atual} kg.")
        else:
            print(f"❌ {RED}Não é possível descarregar {peso} kg. O caminhão possui apenas {self.carga_atual} kg.{RESET}")


    def exibir_informacoes(self):
        nome_motorista = self.motorista.nome if self.motorista else "Sem motorista atribuído"
        print("-" * 40)
        print(f"Caminhão: Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Capacidade de carga: {self.capacidade_carga} kg")
        print(f"Carga atual: {self.carga_atual} kg")
        print(f"Motorista: {nome_motorista}")
        print("-" * 40)


if __name__ == "__main__":
    # 1. Criação dos objetos
    # Motoristas (Datas relativas à data de vencimento)
    data_hoje = datetime.now()
    data_vencendo = (data_hoje + timedelta(days=15)).strftime("%d/%m/%Y")
    data_valida = (data_hoje + timedelta(days=180)).strftime("%d/%m/%Y")
    data_vencida= (data_hoje - timedelta(days=10)).strftime("%d/%m/%Y")
    print(f'\ndata_hoje: {data_hoje} data_vencendo: {data_vencendo} data_valida{data_valida} data_vencida {data_vencida}\n')

    m1 = Motorista("João Silva", 42, "1234567890", data_vencendo) # Vence em 15 dias
    m2 = Motorista("Maria Souza", 35, "0987654321", data_valida)   # Válida por mais tempo
    m3 = Motorista('Pedro', 33,'931239-30193',data_vencida)  # Vencida
    # 3 Caminhões
    c1 = Caminhão("Mercedes Benz", "AAA-1234", 10000)
    c2 = Caminhão("Volvo FH", "BBB-5678", 15000)
    c3 = Caminhão("Scania R450", "CCC-9012", 12000)
    c4 = Caminhão('Scania','JHR-2B45',10000,m2)
    # 2. Atribuir motoristas aos caminhões
    c1.motorista_responsavel(m1)
    c2.motorista_responsavel(m2)
    c3.motorista_responsavel(m1)  # Um motorista pode dirigir vários caminhões (m1 atribuído ao c3 também)
    c3.motorista_responsavel(m3)
    print("=== SIMULAÇÃO DE CARGA E DESCARGA ===")
    c1.carregar(5000)   # Sucesso
    c1.carregar(6000)   # Erro (Excede 10.000 kg)
    c1.descarregar(2000) # Sucesso, sobra 3000 kg
    c1.descarregar(5000) # Erro (Excede Total de carga no Caminhão)

    print("\n=== VERIFICAÇÃO DE CNH DOS MOTORISTAS ===")
    caminhoes = [c1, c2, c3,c4] # lista com os objetos Caminhoes
    motoristas = [m1, m2,m3] # lista com os objetos dos Motoristas

    for m in motoristas: # percorre a lista para cada Objeto motorista em m
        m.verificarValidade()
        # Verifica se está associado a algum caminhão
        caminhoes_do_motorista = [c.placa for c in caminhoes if c.motorista == m]
        if caminhoes_do_motorista:
            print(f"  -> {m.nome} está associado aos caminhões de placa: {', '.join(caminhoes_do_motorista)}")

    print("\n=== INFORMAÇÕES DOS CAMINHÕES E SEUS MOTORISTAS ===")
    for c in caminhoes:
        c.exibir_informacoes()
