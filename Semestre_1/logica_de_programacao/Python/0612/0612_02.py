def ler_string(mensagem):
    return input(mensagem)

x = ler_string("Digite seu nome: ")
print(x)
print(ler_string("Digite seu endereço: "))

lista = []
mensagens = ["Digite seu nome: ", "Digite seu endereço: "]

for i in mensagens:
    x = ler_string(i)
    print(x)



