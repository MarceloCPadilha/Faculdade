class Receita:

    def __init__(self, nome, porcoes_base, tempo_prep, tempo_coccao, ingredientes, passos, custo_por_porcao = 15.00):
        self.nome = nome
        self.porcoes_base = porcoes_base
        self.tempo_prep = tempo_prep
        self.tempo_coccao = tempo_coccao
        self.ingredientes = ingredientes
        self.passos = passos
        self.custo_por_porcao = custo_por_porcao

    def calcular_fator(self, porcoes_desejadas):
        if porcoes_desejadas <= 0:
            raise ValueError("O número de porções deve ser maior que zero.")
        return porcoes_desejadas / self.porcoes_base

    def calcular_tempo_total(self):
        return self.tempo_prep + self.tempo_coccao

    def calcular_custo_estimado(self, porcoes_desejadas):
        return porcoes_desejadas * self.custo_por_porcao

    def exibir_ficha_tecnica(self, chef_nome, porcoes_desejadas):
        fator = self.calcular_fator(porcoes_desejadas)
        tempo_total = self.calcular_tempo_total()
        custo_total = self.calcular_custo_estimado(porcoes_desejadas)

        print("\n" + "-" * 60)
        print("FICHA TÉCNICA DIGITAL (POO) REFEIÇÕES PRÁTICAS".center(60))
        print("-" * 60)
        print("RECEITA: {}".format(self.nome))
        print("Chefe Responsável: {}".format(chef_nome))
        print("Rendimento: {} porção(ões)".format(porcoes_desejadas))
        print("Tempo total de preparo: {} minutos".format(tempo_total))
        print("Custo estimado de produção: R$ {:.2f}".format(custo_total))
        print("-" * 60)
        print("INGREDIENTES NECESSÁRIOS:")

        for item in self.ingredientes:
            qtd_ajustada = item["qtd"] * fator
            if item["unidade"]:
                print(
                    "  - {:.1f} {} {}".format(
                        qtd_ajustada, item["unidade"], item["nome"]
                    )
                )
            else:
                print("  - {}".format(item["nome"]))

        print("\n")
        print("PASSO A PASSO:")
        for idx, passo in enumerate(self.passos, 1):
            print("  {}. {}".format(idx, passo))
        print("=" * 60 + "\n")


def obter_entrada_valida():
    nome = input("Digite seu nome: ").strip()
    while not nome:
        nome = input("O nome não pode estar em branco. Digite seu nome: ").strip()

    while True:
        try:
            porcoes = int(
                input("Quantas porções você deseja preparar? ").strip()
            )
            if porcoes <= 0:
                print("Por favor, digite um número inteiro maior que zero.")
                continue
            return nome, porcoes
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

if __name__ == "__main__":
    ingredientes_peixe = [
        {
            "qtd": 1.0,
            "unidade": "filé(s)",
            "nome": "de peixe fresco (tilápia)"
        },
        {
            "qtd": 2.0,
            "unidade": "batata(s)",
            "nome": "média(s) com casca"
        },
        {
            "qtd": 1.0,
            "unidade": "limão",
            "nome": "(ões)"
        },
        {
            "qtd": 1.0,
            "unidade": "cenoura(s)",
            "nome": "média(s) em tiras finas"
        },
        {
            "qtd": 1.0,
            "unidade": "abobrinha(s)",
            "nome": "pequena(s) em tiras finas"
        },
        {
            "qtd": 0,
            "unidade": "",
            "nome": "Azeite, sal e pimenta-do-reino a gosto"
        }
    ]

    passos_peixe = [
        "Tempere o peixe e deixe marinar por 15 min.",
        "Forre a assadeira com papel manteiga e monte a base de batatas.",
        "Posicione o peixe e cubra com os legumes em tiras.",
        "Feche o papelote e asse a 180°C por 6 minutos. Sirva quente."
    ]

    receita_peixe = Receita(
        nome = "Filé de Peixe no Papelote com Legumes",
        porcoes_base = 1,
        tempo_prep = 30,
        tempo_coccao = 6,
        ingredientes = ingredientes_peixe,
        passos = passos_peixe,
        custo_por_porcao = 18.50
    )

    print("--- INICIALIZANDO CALCULADORA DE PORÇÕES ---")
    chef, num_porcoes = obter_entrada_valida()
    receita_peixe.exibir_ficha_tecnica(chef, num_porcoes)