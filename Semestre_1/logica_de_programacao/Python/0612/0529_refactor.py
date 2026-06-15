"""
Competências a serem observadas:
- Conhecer os comandos/funções utilizados.
- Saber utilizar os comandos/funções corretamente
- Desenvolver uma solução viável 

Observações:
- Salve o código com o seu nome.
- Dentro do programa, coloque o seu nome como comentário.
- Se fizer o código em alguma plataforma, exporte e envie o arquivo .py
- Você deverá realizar a tarefa individualmente.
- Você pode consultar todos os materiais, só não pode utilizar a IA para realizar código.
- Caso faça perguntas para a IA, coloque os prompts como comentário no final do código. 


"""
"""
Enunciado
Implemente um programa em Python que manipule uma lista de números inteiros por meio de um menu interativo. O programa deve permitir ao usuário:
Adicionar número: inserir um novo valor inteiro na lista.
Remover número: excluir um valor específico informado pelo usuário.
Alterar elemento: substituir o valor de um elemento existente por outro.
Localizar elemento: buscar um número na lista e mostrar o índice correspondente.
Consultar por índice: dado um índice, mostrar o elemento armazenado.
Somar elementos: ler dois índices e mostrar a soma dos elementos correspondentes.
O programa deve:
Exibir sempre o conteúdo atual da lista antes de mostrar o menu.
Tratar erros de entrada (ex.: valores não numéricos ou índices inexistentes).
"""

lista = [2, 3, 3, 4]

# =========================================================

def print_list_indexes(lista):
    return ["Index: {}, numero: {}".format(index, number)for index, number in enumerate(lista)]

def validar_numero(numero, lista):
    if numero in lista:
        return True, numero # Número está na lista
    return False, numero, print("Número não está na lista.") # Número não está na lista

def remover(lista):
    numero_ok, numero_correto = validar_numero(numero_valido("Index do número a ser removido: "), lista)
    if numero_ok:
        return lista.pop(numero_correto)

def numero_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except:
            print("OPS. ")

def adicionar(lista):
    return lista.append(numero_valido("Número a ser adicionado: "), lista)

def substituir(lista):
    numero = numero_valido("Número a entrar: ")
    index = numero_valido("Index do numero a ser substituido: ")
    lista[index] = numero

def localizar_e_mostrar_index(lista):
    numero_ok, x = validar_numero(numero_valido("Número a ser localizado e ter o index retornado: "), lista)
    if numero_ok:
        return print(*("indice: {} número: {}\n".format(i, lista[i]) for i in range(len(lista)) if x == lista[i]))

# =========================================================

menu = """
    Menu
    ------------------------------------------------
        1- Adicionar um número na lista
        2- Retirar um número da lista
        3- Alterar um elemento da lista
        4- Localizar um elemento e mostrar o seu indice
        5- Ler um indice e mostrar o elemento
        6- ler dois indices e mostrar a soma dos elementos;
    Escolha: """

while True:
    current_indexes = print_list_indexes(lista)
    print(lista)
    try: 
        escolha = int(input(menu))
    except ValueError:
        print("Digite um valor válido.")
        continue
    match escolha:
        case 1:
            adicionar(lista)
        case 2:
            print(current_indexes)
            remover(lista)
        case 3:
            print(current_indexes)
            substituir(lista)
        case 4:
            localizar_e_mostrar_index(lista)
        case 5:
            try: 
                x = int(input("Digite um indice para receber o número: "))
                if x not in lista:
                    raise ValueError
                print(lista[x])
            except ValueError:
                print("Insira um valor válido.")
                continue
        case 6:
            try: 
                x = int(input("Digite o primeiro indice: "))
                y = int(input("Digite o segundo indice: "))
                print("{} + {} = {}".format(lista[x], lista[y], lista[x] + lista[y]))
            except ValueError:
                print("Digite um valor válido.")
                continue
            except IndexError:
                print("List index out of range.")
                continue
