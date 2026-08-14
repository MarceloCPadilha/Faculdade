# 📝 Exercício Prático: Calculadora de Desconto da
# ByteShop
# 🎯 Objetivo:
# Praticar a criação de funções em Python com parâmetros, retorno de valores e estruturas
# condicionais simples.
# 📄 Contexto do Problema:
# A loja de eletrônicos ByteShop está oferecendo descontos especiais para seus clientes. Para
# agilizar o atendimento no caixa, você foi contratado para criar um pequeno script em Python
# que calcule o valor final das compras após a aplicação do desconto.
# 💻 Requisitos do Exercício:
# 1. Crie uma função chamada calcular_desconto que receba dois parâmetros:
# ○ valor_compra (float): O valor total da compra em reais.
# ○ cupom (string): O código do cupom de desconto digitado pelo cliente.
# 2. Regras do Cupom de Desconto:
# ○ Se o cupom for "DESCONTO10", a função deve aplicar 10% de desconto sobre o valor
# da compra.
# ○ Se o cupom for "DESCONTO20", a função deve aplicar 20% de desconto sobre o valor
# da compra.
# ○ Se o cupom for qualquer outro valor (ou vazio), nenhum desconto deve ser aplicado
# (0%).
# 3. Retorno da Função:
# ○ A função deve calcular e retornar (return) apenas o valor final da compra já com o
# desconto aplicado.
# 4. Programa Principal (Testes):
# ○ Escreva um programa principal que chame a função pelo menos três vezes com valores
# e cupons diferentes e imprima o resultado na tela de forma organizada.
# 💡 Exemplo de Entrada e Saída Esperada:
# Python
# # Chamadas da função no programa principal:
# valor1 = calcular_desconto(100.0, "DESCONTO10")
# valor2 = calcular_desconto(200.0, "DESCONTO20")
# valor3 = calcular_desconto(150.0, "SEMDESCONTO")
# # Impressão dos resultados:
# # Compra de R$ 100.00 com 'DESCONTO10' -> Valor final: R$ 90.00
# # Compra de R$ 200.00 com 'DESCONTO20' -> Valor final: R$ 160.00
# # Compra de R$ 150.00 com 'SEMDESCONTO' -> Valor final: R$ 150.00
# 🌟 Desafio Extra (Opcional):
# Modifique a função para que ela também aceite cupons digitados em letras minúsculas (ex:
# "desconto10"), utilizando o método .upper() para tratar o texto.

def traducao_coupon(coupon):
    coupons = {"DESCONTO10": 0.90, "DESCONTO20": 0.80}
    while True:
        try:
            return coupons[coupon.upper()]
        except:
            print("Digite um coupom válido")
            return 1

def calcular_desconto(valor_compra, coupon):
    return valor_compra * traducao_coupon(coupon)

valor1 = calcular_desconto(100.0, "DESCONTo10")
valor2 = calcular_desconto(200.0, "DESCONTO10")
valor3 = calcular_desconto(2000.0, "DESCONTO10")

print(valor1)
print(valor2)
print(valor3)