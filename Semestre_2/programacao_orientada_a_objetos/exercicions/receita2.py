class Receita:

    def __init__(self, nome, porcoes_base, tempo_prep, tempo_coccao, ingredientes, passos, custo_por_porcao = 12.00):
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

        print("-" * 60)
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
    ingredientes_spaghetti = [
        {
            "qtd": 2.0,
            "unidade": "unidade(s)",
            "nome": "de abobrinha verde grande"
        },
        {
            "qtd": 300.0,
            "unidade": "g",
            "nome": "de carne moída magra (patinho)"
        },
        {
            "qtd": 2.0,
            "unidade": "xícara(s)",
            "nome": "de molho de tomate natural"
        },
        {
            "qtd": 2.0,
            "unidade": "dente(s)",
            "nome": "de alho picado"
        },
        {
            "qtd": 0.5,
            "unidade": "unidade(s)",
            "nome": "de cebola média picada"
        },
        {
            "qtd": 0,
            "unidade": "",
            "nome": "Azeite de oliva, folhas de manjericão, sal e pimenta a gosto"
        }
    ]

    passos_spaghetti = [
        "Fatie as abobrinhas no espiralizador para formar os fios do spaghetti.",
        "Em uma panela, refogue o alho e a cebola no azeite até dourar.",
        "Adicione a carne moída e cozinhe até dourar bem; acerte o sal e a pimenta.",
        "Incorpore o molho de tomate e deixe apurar por 10 minutos em fogo baixo.",
        "Manteigue rapidamente o spaghetti de abobrinha na frigideira por 2 minutos.",
        "Sirva o spaghetti coberto com o molho bolonhesa e decore com manjericão."
    ]

    receita_spaghetti = Receita(
        nome = "Spaghetti de Abobrinha ao Molho Bolonhesa",
        porcoes_base = 2,
        tempo_prep = 15,
        tempo_coccao = 15,
        ingredientes = ingredientes_spaghetti,
        passos = passos_spaghetti,
        custo_por_porcao = 12.00
    )

    print("--- INICIALIZANDO CALCULADORA DE PORÇÕES ---")
    chef, num_porcoes = obter_entrada_valida()
    receita_spaghetti.exibir_ficha_tecnica(chef, num_porcoes)