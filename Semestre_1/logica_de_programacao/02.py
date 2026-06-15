from math import sqrt, factorial

def ramanujan_The_Goat(termo=1):
    somatorio = 0
    
    fator_externo = (2 * sqrt(2))/9801
    
    # somatorio
    for n in range(termo):
        numerador = factorial(4*n) * (1103 + (26390 * n))
        denominador = ((factorial(n)) ** 4) * (396**(4*n))
        somatorio += numerador / denominador 
        
    um_pra_pi = fator_externo * somatorio
        
    pi_final = 1 / um_pra_pi
    
    return pi_final

print("{:.15f}".format(ramanujan_The_Goat(10)))