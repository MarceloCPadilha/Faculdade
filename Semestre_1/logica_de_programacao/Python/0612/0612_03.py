lista = []

def validar_numero(numero):
    if numero in lista:
        return True, numero # Número está na lista
    return False, numero # Número não está na lista

def remover():
    numero_ok, numero_correto = validar_numero(numero_valido("Número a ser removido: "))
    if numero_ok:
        lista.remove(numero_correto)

def numero_valido(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except:
            print("OPS. ")

def adicionar():
    return lista.append(numero_valido("Número a ser adicionado: "))

print(lista)
adicionar()
print(lista)
remover()
print(lista)