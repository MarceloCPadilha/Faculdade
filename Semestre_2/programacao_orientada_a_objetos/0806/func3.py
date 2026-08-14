def soma():
    while True:
        try:
            n1 = int(input("Digite um valor: "))
            n2 = int(input("Digite outro valor: "))
            break
        except:
            print("Criatura digite valores int")
    return (n1 + n2)

# Início Programa
for i in range(5):
    print("A soma é {}".format(soma()))