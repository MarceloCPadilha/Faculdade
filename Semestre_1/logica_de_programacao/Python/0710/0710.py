# Avaliação 02
# Favor salvar o código com o seu nome
# Nome: 
#
# Competências avaliadas:
# - Conhecer os comandos básicos da linguagem
# - Saber utilizar corretamente os comandos
# - Desenvolver uma solução viável e adequada para o problema proposto.

# Faça um algoritmo que realize a avaliação de seus professores conforme o menu abaixo.
# MENU
# 1- cadastro de aluno
# 2- avaliação do Professor
# 3- relatório
# Escolha: 

# Utilize a seguinte lista de professores
# lstProfessores  = [   "Ivonei Marques" ,
#                     "Roberto Oliveira",
#                     "Julio Carnevalle",
#                     "Rafael Rehm",
#                     "Fabio Giulian"
#                   ]
# Use a seguinte lista para cadastro de alunos:
# lstAlunos = []
# Use a seguinte lista para dar a nota:
# lstNotas  = [0,0,0,0,0]
# Obs: A correlação entre lstPrefessores e lstNotas acontece pelo índice.

# Na opção 1 você deverá adicionar o nome do aluno em lstAluno.
#         Critérios:  - Nome não deve ter menos de 3 caracteres
#                     - Nome deve ter apenas letras e espaços em branco
#                     - É necessário ter alunos cadastrados antes de poder avaliar os professores.
# Na opção 2  o aluno deverá dar uma nota de 1 a 5 para APENAS UM dos Professores
#             escolhido pelo aluno.
#         - Escolha um aluno Cadastrado   
#         - Escolha um professor
#         - Dar a nota ao professor (acumular a nota em lstNotas)
#         Critérios:  - Validar nota. Não deixar o aluno votar mais de uma vez.
#                     - A nota deve estar na faixa de 1 a 5. (1- Pior Nota,  5- Melhor Nota)
#                     - Caso todos alunos já tenham votado, exibir a seguinte mensagem:
#                         "Todos alunos já votaram."
# Na opção 3 você deverá listar os prefessores e suas avaliações,
#         calculando o percentual da nota conforme Exemplo:
#         ----------------------------------------------------
#         Professor                    Nota    Perc
#         Ivonei Marques               34      22.5
#         Roberto Oliveira             40      26.5
#         Julio Carnevalle             19      12.6
#         Rafael Rehm                  37      24.5
#         Fabio Giulian                21      13.9
#         ----------------------------------------------------


lstProfessores = ["Ivonei Marques" ,
                  "Roberto Oliveira",
                  "Julio Carnevalle",
                  "Rafael Rehm",
                  "Fabio Giulian"
                ]
# expected values [nome, ja_votou]
lstAlunos = [["Primeiro Aluno", False]]
lstNotas  = [0,0,0,0,0]


def print_menu(lista):
    print(*("{} - {}\n".format(i, lista[i])for i in range(len(lista))), sep="", end="")

def numero_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número.")
            
def validar_indice(numero, lista):
    if 0 <= numero < len(lista):
        return True, numero
    return False, numero

def nome_valido():
    while True:
        erros = []
        try:
            nome = str(input("Digite o nome do aluno: "))
            if len(nome) < 3:
                erros.append("Nome muito curto.")
            if not nome.replace(" ", "").isalpha():
                erros.append("Nome deve conter apenas letras e espaços em branco.")
            if erros:
                raise ValueError
            else:
                return nome
        except ValueError:
            for i in erros:
                print(i, end="\n")

def nota_valida():
    while True:
        try:
            erros = []
            nota = numero_valido("Digite uma nota de 1 a 5 (1- Pior Nota,  5- Melhor Nota)\nNota: ")
            if nota < 1 or nota > 5:
                erros.append("Nota fora do intervalo aceitavel. ")
            if erros:
                raise ValueError
            else:
                return nota
        except ValueError:
            for i in erros:
                print(i, end="\n")

def todos_ja_votaram(lst_alunos):
    for i in range(len(lst_alunos)):
        if lst_alunos[i][1] == False:
            return False
    return True

def menu1():
    while True:
        lstAlunos.append([nome_valido(), False])
        print(lstAlunos)
        print()
        break

def menu2():
    while True:
        if not lstAlunos:
            print("Não tem alunos.")
            break
        if todos_ja_votaram(lstAlunos):
            print("Todos alunos ja votaram.")
            break
        nota = 0
        print()
        print_menu(lstAlunos)
        aluno_ok, aluno = validar_indice(numero_valido("Escolha o aluno para avaliar: "), lstAlunos)
        print(aluno_ok, aluno)
        if aluno_ok:
            if lstAlunos[aluno][1] != True:
                print()
                print_menu(lstProfessores)
                professor_ok, professor = validar_indice(numero_valido("Escolha um professor para avaliar: "), lstProfessores)
                if professor_ok:
                    nota = nota_valida()
                    lstNotas[professor] += nota
                    lstAlunos[aluno][1] = True
                print()
            else:
                break
            break

def menu3():
    nota = False
    for i in lstNotas:
        if i != 0:
            nota = True
    if nota == True:
        print("----------------------------------------------------\n"
            "Professor                    Nota    Perc\n"
            "Ivonei Marques               {}      {:02f}\n"
            "Roberto Oliveira             {}      {:02f}\n"
            "Julio Carnevalle             {}      {:02f}\n"
            "Rafael Rehm                  {}      {:02f}\n"
            "Fabio Giulian                {}      {:02f}\n"
            "----------------------------------------------------"
            .format(
                lstNotas[0], (lstNotas[0] / sum(lstNotas)) * 100,
                lstNotas[1], (lstNotas[1] / sum(lstNotas)) * 100,
                lstNotas[2], (lstNotas[2] / sum(lstNotas)) * 100,
                lstNotas[3], (lstNotas[3] / sum(lstNotas)) * 100,
                lstNotas[4], (lstNotas[4] / sum(lstNotas)) * 100))
    else:
        print("Nenhum professor foi avaliado.")

def menu():
    while True:
        escolha = numero_valido("1- cadastro de aluno\n2- avaliação do Professor\n3- relatório\nEscolha: ")
        if escolha == 1:
            menu1()
        elif escolha == 2:
            menu2()
        elif escolha == 3:
            menu3()
        else:
            print("Escolha um número valido")

def main():
    menu()

main()
