# Escrever um algoritmo que leia, para um número não determinado de alunos, as 3 notas obtidas por cada aluno.
# Calcular a média de aproveitamento, usando a fórmula:
# MA = ( Nota1 + Nota2 x 2 + Nota3 x 3 ) / 6

# A atribuição de conceitos obedece a tabela abaixo:
# Média de Aproveitamento - Conceito
# 9,0 e <= 10,0                         - A
# 7,5 e < 9,0                             - B
# 6,0 e < 7,5                             - C
# 4,0 e < 6,0                             - D
# < 4,0                                      - E
# O algoritmo deve escrever o número do aluno, suas notas, a média de aproveitamento, o conceito correspondente e a 
# mensagem: APROVADO se o conceito for A,B ou C e REPROVADO se o conceito for D ou E.

# estrutura esperada
alunos = []
# alunos = [
#     {
#         "aluno": "Aluno 1",
#         "notas": [10, 10, 10],
#         "media": 10
#     }
# ]

def media_ponderada_com_peso_de_aumento_linear(*notas):
    peso_total = 0
    nota_ponderada = 0
    for peso, nota in enumerate(notas, start=1):
        peso_total += peso
        nota_ponderada += nota * peso

    return nota_ponderada / peso_total

def definir_conceito(media):
    if media >= 9:
        return "A"
    elif 7.5 < media < 9:
        return "B"
    elif 6.0 < media < 7.5:
        return "C"
    elif 4.0 < media < 6.0:
        return "D"
    elif media < 4.0:
        return "E"
    
def aprovacao(conceito):
    aprovado = ("A", "B", "C")
    if conceito in aprovado:
        return "APROVADO"
    return "REPROVADO"

        
def print_alunos(*alunos):
    for aluno in alunos:
        print("Aluno: {}\nNotas: {}\nMédia: {}\nSituação curricular: {}"
              .format(aluno["aluno"], aluno["notas"], aluno["media"], aprovacao(definir_conceito(aluno["media"]))))

def ler():
    count = 1
    qntd_notas = 3
    
    while True:
        escolha = str(input("Desejá encerrar? (digite 'y' se sim)")).upper()
        if escolha == "Y":
            break
        
        notas = []

        aluno = "Aluno {}".format(count)
        count += 1

        for i in range(qntd_notas):
            nota = float(input("Digite a {}ª nota: ".format(i + 1)))
            notas.append(nota)
        
        alunos.append({
            "aluno": aluno,
            "notas": notas,
            "media": media_ponderada_com_peso_de_aumento_linear(*notas)
            })

ler()
print_alunos(*alunos)

# Dicionários são um estrutura de dados em python que funcionam de forma similar a uma lista, 
# com uma key/chave e um value/valor associado a essa chave, a diferença é que nos dicionarios essa key é definida na criação
# e tu não pode chamar o valor do dicionario iterando sobre ele e chamando keys numericas como em listas.

# ex: 
# aluno = { "aluno": "Aluno 1", "notas": [10, 10, 10], "media": 10 }
# print(aluno["aluno"], aluno["notas"], aluno["media"]) # output: Aluno 1 [10, 10, 10] 10
# alterar valor:
# aluno["aluno"] = "aluno 3"

# tu também pode fazer nested dictionaries, que são dicionarios dentro de dicionarios
# alunos = { "aluno 1": { "nome": "guilherme", "notas": [10, 10, 10], "media": 10 },
#            "aluno 2": aluno = { "nome": "joao", "notas": [10, 10, 10], "media": 10 }}
# print(alunos["aluno 1"]["nome"]) # output: guilherme
# para alterar valor:
# alunos["aluno 1"]["media"] = 0
# alunos["aluno 2"]["media"] = 0

# python também tem algumas metodos de dicionários built-in, como 
# .pop() para remover um item

# .update() se tu quiser mudar algo 
# aluno["aluno"] = "aluno 3" | é a mesma coisa que | # aluno.update({"aluno": "aluno 3"})

# os proximos 3 metodos são uteis para manipulação e iteração sobre dicionarios
# .key() para retornar uma lista com o valor das keys do dicionario
# aluno = { "aluno": "Aluno 1", "notas": [10, 10, 10], "media": 10 }
# keys = aluno.keys() # output: dict_keys(['aluno', 'notas', 'media'])

# .values() para retornar uma lista com os valores do dicionario
# aluno = { "aluno": "Aluno 1", "notas": [10, 10, 10], "media": 10 }
# keys = aluno.keys() # output: dict_values(['Aluno 1', [10, 10, 10], '10'])

# .items() para retornar uma lista os itens do dicionario
# aluno = { "aluno": "Aluno 1", "notas": [10, 10, 10], "media": 10 }
# keys = aluno.keys() # output: dict_items([("aluno": "Aluno 1"), ("notas": [10, 10, 10]), ("media": 10)])

# .copy, para copiar um dicionario
# dict1 = {}
# dict2 = dict1.copy()
# ou
# dict2 = dict(dict1)

# .clear()
# aluno = { "aluno": "Aluno 1", "notas": [10, 10, 10], "media": 10 }
# aluno.clear()
# print(aluno) # output: {}
# ou seja, aluno = {}
