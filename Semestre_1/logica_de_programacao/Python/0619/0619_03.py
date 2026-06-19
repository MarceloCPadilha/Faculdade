# Faça um Programa que leia vários números inteiros, limitando a lista em 8 elementos
# e armazene-os em uma lista.
# Quando a lista chegar no limite, o primeiro elemento deve ser eliminado.
def input_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número válido.")
            continue

def ler():
    limite_da_lista = 8
    indice = 0
    lista = []
    if len(lista) < limite_da_lista:
        for i in range(limite_da_lista):
            x = input_valido("Digite o {}° número: ".format(indice + 1))
            lista.append(x)
            print(lista)
    while True:
        x = input_valido("Digite o {}° número: ".format(indice + 1))
        lista[indice] = x
        indice = (indice + 1) % limite_da_lista
        print(lista)

ler()