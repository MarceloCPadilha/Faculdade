"""
Usei IA pra tirar umas duvidas sobre acesso a itens em nested dictionaries pra printar em for loops
nota: lembrar de nunca mais usar dicionarios

SIMULADO.

Competências a serem observadas:
- Conhecer os comandos/funções utilizados.
- Saber utilizar os comandos/funções corretamente
- Desenvolver uma solução viável 

Faça um algoritmo que leia o nome de até 10 professores.
Cada professor da lista receberá uma nota entre 1 e 5 de uma turma com 8 alunos.
Mostre o nome do professor a soma de suas notas e também a média de notas de cada professor em ordem crescente..

Observações:
Você deverá realizar a tarefa individualmente / grupo.
Caso tenha dificuldades, pode fazer juntamente com um colega.
     - Entregue apenas um código com o nome dos participantes.
     - Indique quem desenvolveu o código

Coloque uma observação no início do código dizendo se você utilizou ou não IA na solução.

"""

# tire o comentario do valor dentro do dict_prof e coloque o primeiro for loop inteiro dentro de um comentario pra testar
dict_prof = {
     # 'prof1': {'nome': 'prof1', 'nota_soma': 40, 'nota_media': 1.0}, 'prof2': {'nome': 'prof2', 'nota_soma': 40, 'nota_media': 2.0}, 'prof3': {'nome': 'prof3', 'nota_soma': 40, 'nota_media': 3.0}, 'prof4': {'nome': 'prof4', 'nota_soma': 40, 'nota_media': 4.0}, 'prof5': {'nome': 'prof5', 'nota_soma': 40, 'nota_media': 5.0}, 'prof6': {'nome': 'prof6', 'nota_soma': 40, 'nota_media': 1.0}, 'prof7': {'nome': 'prof7', 'nota_soma': 40, 'nota_media': 2.0}, 'prof8': {'nome': 'prof8', 'nota_soma': 40, 'nota_media': 3.0}, 'prof9': {'nome': 'prof9', 'nota_soma': 40, 'nota_media': 4.0}, 'prof10': {'nome': 'prof10', 'nota_soma': 40, 'nota_media': 5.0}
}
qntd_professores = 10
qntd_alunos = 8

for professor in range(1, qntd_professores + 1):
     soma_notas = 0
     nome_do_professor = input("Digite o nome do {}º professor: ".format(professor))
     for aluno in range(1, qntd_alunos + 1):
          nota = int(input("Digite a {}ª nota: ".format(aluno)))
          soma_notas = soma_notas + nota
          if nota > 5 or nota < 1:
               print("valor errado")
               exit()

     media_notas = soma_notas / qntd_alunos
     nome_variavel = "prof{}".format(professor)

     dict_prof[nome_variavel] = {"nome" : nome_do_professor, "nota_soma" : soma_notas, "nota_media" : media_notas}


sort = sorted(dict_prof.values(), key=lambda j: j["nota_media"])

print("\n\n")

for i in sort:
     print("nome:", i["nome"], "\n" "nota_soma", i["nota_soma"], "\n" "nota_media:", i["nota_media"])
     print()
