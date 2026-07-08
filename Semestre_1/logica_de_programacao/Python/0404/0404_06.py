# Exercício 06.
# Faça um algoritmo para ler 5 números inteiros. Após imprima a seguinte mensagem: "A quantidade de números pares é:",  qt_pares, ou "Nenhum número par foi digitado"

from random import randint

numeros = [randint(0, 100) for _ in range(0, 5)]
# numeros = [1, 3, 5, 7, 9] # zero pares, tira o comentario pra testar com 0 pares

qt_pares = sum(1 for i in numeros if i % 2 == 0)

print(numeros)
print("A quantidade de números pares é: {}".format(qt_pares) if qt_pares > 0 else "Nenhum número par foi digitado")