# Funções
# parâmetros, localidade das variaveis

def nome_func(texto, numero):
    # aqui ele define v1 como global então quando a função é executada o valor da v1 global recebe 222
    global v1
    v2 = "Brownies"
    v1 = 222
    print(texto, "gosta de", v2)
    print(numero * 2)
    print(v1)
    return "Executado."

def nome_func2():
    print("ccc")

# essa variavel é global então é diferente da instanciada localmente dentro da função
v1 = "Cookies"
print("aaaa")
x = nome_func("Marcelo", 77)
print(v1)
print(x)

