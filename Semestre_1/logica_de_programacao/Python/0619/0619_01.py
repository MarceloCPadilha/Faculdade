# Faça um Programa que leia 20 números inteiros
# e armazene-os em uma lista.
# Leia a lista anterior e copie os números pares para a lista uma lista PAR
# e os números impares uma lista IMPAR.
# Imprima os três vetores(listas).
def ler_20_numeros():
    lista = []
    count = 0
    while True:
        try:
            x = int(input("Digite o {}° número: ".format(count+1)))
            count += 1
        except ValueError:
            print("Digite um valor do tipo adequado.")
        lista.append(x)
        if count == 20:
            break
    return lista

def copiar_pares(lista):
    lista_copia = [i for i in lista if i % 2 == 0]
    return lista_copia

def copiar_impares(lista):
    lista_copia = [i for i in lista if i % 2 != 0]
    return lista_copia

lista = ler_20_numeros()
lista_par = copiar_pares(lista)
lista_impar = copiar_impares(lista)

print("Lista original: \n{}\n".format(lista))
print("Lista par: \n{}\n".format(lista_par))
print("Lista impar: \n{}\n".format(lista_impar))