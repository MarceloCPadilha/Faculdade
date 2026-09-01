# definição da classe
class Conta:
    # definição dos atributos
    numero = 0
    saldo = 0.0
    # definição de método
    def abertura(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo       
        print("Conta aberta com sucesso!")
    def listar(self):
        print("Numero: {}".format(self.numero))
        print("Saldo: {}".format(self.saldo))
                

usuario_conta = Conta()
# usuario_conta.numero = 0o00000000
# usuario_conta.saldo = 1000.0
usuario_conta.abertura(0o00000000, 1000.0)

outro_usuario_conta = Conta()
outro_usuario_conta.abertura(0o00000001, 1000.0)

# transferencia bancaria
usuario_conta.saldo -= 100
outro_usuario_conta.saldo -= 100

#transferencia de uma conta para outra

print('********** Conta **********')
usuario_conta.listar()

print('\n********** Outra Conta **********')
outro_usuario_conta.listar()