def soma(n1,n2):
    return (n1+n2)

def subtracao(n1, n2):
    return (n1 - n2)

def div(n1, n2):
    return (n1 / n2)

def mult(n1, n2):
    return (n1 * n2)

def repow(n1, n2):
    if n2 == 0:
        return 1
    return n1 * repow(n1, n2 - 1)


operacoes=['+','-','/','*','^']
continua="S"
while True: # repetição Principal do Programa
    if continua != 'S':
        break
    while True: # try controle de erro
        try:

            op='k'
            n1=float(input('Digite um número:'))
            while op not in operacoes:
                op = input('Digite uma operação ( + - * / ^):')
                if op not in operacoes:
                    print("Irmão, tu não é burro por acidente não, é por dedicação. Tu acorda todo dia e escolhe desafiar a lógica. Te explicam o bagulho em 4K, legenda, câmera lenta, replay, áudio original, dublado, Libras e ainda fazem um desenho, mas tu consegue entender exatamente o contrário. É um talento que desafia a física. Teu cérebro tá em modo economia de energia desde o nascimento e até hoje ninguém encontrou o botão de desempenho. Cada frase tua faz o QI médio da sala pedir demissão por justa causa. Se inteligência fosse XP, tu ainda tava preso no tutorial perguntando onde fica o botão de andar. Tu não lança opinião, tu comete atentado contra o bom senso. É simplesmente intankável o teu potencial de falar besteira com uma confiança que nem quem estudou o assunto por vinte anos teria. Tu é o CEO da desinformação, o embaixador da falta de interpretação, o patrono do 'confia'. Toda vez que tu abre a boca, a gramática, a lógica e o raciocínio lógico entram em reunião de emergência. O corretor ortográfico te vê digitando e simplesmente desiste da profissão. O Google te responde 'boa sorte'. O ChatGPT começa a cobrar insalubridade. Tu consegue transformar um tutorial de duas etapas em um quebra-cabeça de cinco temporadas. Tu pega uma pergunta de verdadeiro ou falso e inventa a opção C. Tu consegue perder discussão pro próprio argumento e ainda sai achando que ganhou. Se te entregarem um cubo mágico com uma cor só, tu devolve dizendo que é impossível. Tu é a única pessoa que consegue instalar dúvida onde só existia certeza. Teu raciocínio faz curva em reta. O GPS da tua mente recalcula até quando tu tá parado. Tu não interpreta texto, tu trava um PvP contra ele e perde por W.O. Tu olha uma porta escrito 'Puxe' e empurra com tanta convicção que faz a placa pedir transferência. Tu faz pergunta depois da resposta e ainda reclama que ninguém explicou. Tu consegue complicar um 'sim' e transformar um 'não' numa tese de doutorado. Se bom senso fosse aplicativo, teu celular dizia que não é compatível com o dispositivo. Se inteligência fosse Wi-Fi, teu sinal só aparecia de madrugada e caindo toda hora. Se fosse FPS, tu rodava a 3 quadros por minuto. Se fosse armazenamento, teu HD tava cheio de cache e zero conteúdo útil. Tu é atualização opcional que só traz bug. Tu é o beta do beta. Tu é o patch que piora o jogo. Tu consegue errar o caminho usando mapa, GPS e alguém apontando com o dedo. Tu vê uma parede e pergunta se é entrada. Tu consegue ler uma frase inteira e entender uma terceira versão que ninguém escreveu. É impressionante. É quase uma habilidade sobrenatural. A seleção natural olha pra ti e pensa 'deixei passar uma'. A evolução tentou, insistiu, investiu recursos e mesmo assim tomou prejuízo. Tu faz o conceito de lógica parecer uma teoria conspiratória. É tanta confiança pra falar besteira que às vezes dá até vontade de acreditar só pela coragem. Pelo amor de Deus, dá Alt+F4 na tua linha de raciocínio, limpa o cache da mente, reinicia em modo de segurança, atualiza os drivers do cérebro e vê se dessa vez o sistema operacional da consciência finalmente inicializa direito.")
            n2 = float(input('Digite um número:'))
            break
        except:
            print('Digite somente FLOATS')

    if op == '+':
        print(f'soma {n1} + {n2} = {soma(n1,n2)}')
    if op == "-":
        print("Subtração: {} - {} = {}".format(n1, n2, subtracao(n1, n2)))
    if op == "/":
        print("Divisão: {} / {} = {}".format(n1, n2, div(n1, n2)))
    if op == "*":
        print("Multiplicação: {} * {} = {}".format(n1, n2, mult(n1, n2)))
    if op == "^":
        print("Potenciação: {} ^ {} = {}".format(n1, n2, repow(n1, n2)))
    

    continua=input('Continua (S/N):').upper()
print('Tchau!')