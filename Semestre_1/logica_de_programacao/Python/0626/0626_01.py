
def validar_10_99(n):
    while True:
        try:
            if 10 <= n <= 99:
                return True, n
            raise ValueError
        except ValueError:
            print("Número fora do intervalo.")
            return False, n

def numero_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Input do tipo errado.")

def somar_lista(lista):
    return sum([i for i in lista])

def looping_index(indice, indice_limite):
    return ((indice + 1) % indice_limite)

def ler():
    lista = [00, 00, 00, 00]
    limite_da_lista = 4
    indice = 0
    qntd_zeros = 2
    while True:
        for i in lista:
            print("[ {:0{}d} ]".format(i, qntd_zeros), end="")
        print(" = {:0{}d}".format(somar_lista(lista), qntd_zeros))
        numero_ok, x = validar_10_99(numero_valido("Digite um número entre 10 e 99 para entrar na {}ª posição: ".format(indice + 1)))
        if numero_ok:
            lista[indice] = x
            indice = looping_index(indice, limite_da_lista)        

ler()
