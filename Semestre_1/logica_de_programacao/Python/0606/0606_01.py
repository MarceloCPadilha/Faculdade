# Faça um algoritmo que leia o nome e a idade de um conjunto de nadadores a partir da idade classifica-o em uma das seguintes categorias: infantil A = 5 - 7 anos
# infantil B = 8-10 anos
# juvenil A = 11-13 anos
# juvenil B = 14-17 anos
# adulto = maiores de 18 anos
# O programa deve terminar quando o nome for = “FIM”
# Após a leitura dos dados motre a quantidade de alunos em cada categoria e o percentual da categoria.
# Mostre também o total de alunos de todas as categorias.]

# Para fins de teste. só digitar fim para terminar o loop e o teste sera feito. melhor do que ficar adicionando nadador pra testar
# this_dict = {
#     "infantil_A": 1,
#     "infantil_B": 1,
#     "juvenil_A": 1,
#     "juvenil_B": 1,
#     "adulto": 1
# }
# total_nadadores = 5

this_dict = {
    "infantil_A": 0,
    "infantil_B": 0,
    "juvenil_A": 0,
    "juvenil_B": 0,
    "adulto": 0 
}
total_nadadores = 0

while True:
    nome = input("Digite o nome do nadador. Caso queira terminar o programa digite 'FIM': ").upper()
    if nome == "FIM":
        break

    try:
        idade = int(input("Digite a idade do nadador: "))
        if idade < 5:
            raise ValueError
    except ValueError:
        print("Digite um valor válido")
        continue
    
    if 5 <= idade <= 7:
        this_dict["infantil_A"] += 1
        total_nadadores += 1
        print("Nadador classificado com sucesso")
    elif 8 <= idade <= 10:
        this_dict["infantil_B"] += 1
        total_nadadores += 1
        print("Nadador classificado com sucesso")
    elif 11 <= idade <= 13:
        this_dict["juvenil_A"] += 1
        total_nadadores += 1
        print("Nadador classificado com sucesso")
    elif 14 <= idade <= 17:
        this_dict["juvenil_B"] += 1
        total_nadadores += 1
        print("Nadador classificado com sucesso")
    elif idade >= 18:
        this_dict["adulto"] += 1
        total_nadadores += 1
        print("Nadador classificado com sucesso")

if total_nadadores > 0:
    print("Total de nadadores em todas as categorias: {}\n".format(total_nadadores))
            
    print("Toltal de nadadores por categoria e porcentagem:\n")        
    for i in this_dict.items():
        porcentagem = (i[1] / total_nadadores) * 100
        print("{}: {} aluno(s) - {:.20f}%".format(i[0], i[1], porcentagem))
else:
    print("Nenhum nadador foi classificado.")
