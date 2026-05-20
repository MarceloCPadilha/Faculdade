# Exercício 1:
# Faça um algoritmo que leia uma quantidade indeterminada de números (finalize quando digitado a palavra 'fim')
# No final diga:
# quantos números negativos foram digitados,
# quantos números pares,
# quantos números digitados estão no intervalo de 10 e 30, ou no intervalo de 50 e 70.

negativos = 0
pares = 0
no_intervalo = 0

while True:
    input_ = input("Digite um número (ou 'fim' para encerrar): ").strip().lower()
    
    if input_ == 'fim':
        break
    
    try:
        num = float(input_)
        
        if num < 0:
            negativos += 1

        if num % 2 == 0:
            pares += 1

        if (10 <= num <= 30) or (50 <= num <= 70):
            no_intervalo += 1
            
    except ValueError:
        print("Input inválido. Digite um número ou 'fim'.")

print("{} números negativos foram digitados. \n{} números pares foram digitados. \n{} números digitados estão entre 10-30 ou 50-70"
	.format(negativos, pares, no_intervalo))
