class ContaBancaria:
    
    def __init__(self, titular, saldo):
        self.__titular = titular # Atributo privado
        self.__saldo = saldo # Atributo privado

    def listar_saldo(self):
        print('Titular',self.__titular)
        print('Saldo',self.__saldo,"\n\n")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        self.__saldo += valor
        print("Depósito realizado com sucesso.")

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    
    

cliente1 = ContaBancaria('Gabriel',1000.00)
cliente1.listar_saldo()
cliente1.sacar(100)
cliente1.listar_saldo()

## alteração IMPOSSÍVEL por ser PRIVADO
cliente1.__saldo=2000
print('Não funciona cliente1.__saldo=2000 ')
cliente1.listar_saldo()

cliente1.depositar(1200)
cliente1.listar_saldo()

cliente1.sacar(5000)