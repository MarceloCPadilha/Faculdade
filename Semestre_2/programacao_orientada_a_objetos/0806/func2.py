def alo(nome):
    print("Olá, {}!".format(nome))
    print("Bem-vindo a POO!")
    if nome.upper() == "GABRIEL":
        print("Você é LINDÃO")

while True:
    nome=input("Digite um nome: ")
    if nome.upper() == "FIM":
        break
    alo(nome)

print("Fim do Programa")
