class Proprietario:
    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def exibir_dados(self):
        print("Exibindo dados de {}".format(self.nome))
        print("Nome: {}".format(self.nome))
        print("cpf: {}".format(self.cpf))
        print("telefone: {}".format(self.telefone))
        print("email: {}".format(self.email))
        print()

class Corretor:
    def __init__(self, nome: str, cresci: str, percentual_comissao: float):
        self.nome = nome
        self.cresci = cresci
        self.percentual_comissao = percentual_comissao

    def vender_imovel(self, imovel, proprietario_comprador):
        if imovel.status.lower() != "disponivel":
            print("Imóvel indisponivel para venda.")
            return
        flag = imovel.alterar_proprietario(proprietario_comprador)
        if flag == False:
            print("Proprietaio inválido")
            return

        imovel.alterar_status("Vendido")
        imovel.exibir_ficha()
        print("\nvendido para\n")
        proprietario_comprador.exibir_dados()
        print("Comissão do corretor: {}".format(imovel.valor * (self.percentual_comissao / 100)))

class Imovel:
    status_permitidos = ["disponivel", "alugado", "vendido"]
    tipos_permitidos = ["Casa", "Apartamento"]

    def __init__(self, codigo: int, endereco: str, tipo: str, valor: float, status: str, proprietario: Proprietario, corretor: Corretor):
        self.codigo = codigo
        self.endereco = endereco
        self.tipo = tipo
        self.valor = valor
        self.status = status
        self.proprietario = proprietario
        self.corretor = corretor

    def alterar_status(self, status_novo):
        if status_novo.lower() in self.status_permitidos:
            self.status = status_novo.capitalize()
            print("Status alterado para {}".format(status_novo))
            print()
        else:
            print("Status inválido")
            print()

    def exibir_ficha(self):
        print("Exibindo ficha do Imóvel")

        print("Código: {}".format(self.codigo))
        print("Endereço: {}".format(self.endereco))
        print("Tipo: {}".format(self.tipo))
        print("Valor: {}".format(self.valor))
        print("Status: {}".format(self.status))
        print("Proprietario: {}".format(self.proprietario.nome))
        print("Corretor: {}".format(self.corretor.nome))
        
        print()

    def alterar_proprietario(self, proprietario_novo):
        if proprietario_novo:
            self.proprietario = proprietario_novo
            return True
        else:
            return False

# Instanciando objetos
proprietario1 = Proprietario("prop1", "999999999991", "999999991", "prop1@gmail.com")
proprietario2 = Proprietario("prop2", "999999999992", "999999992", "prop2@gmail.com")

corretor1 = Corretor("corr1", "12345", 6.0)
corretor2 = Corretor("corr2", "12346", 5.0)

imovel1 = Imovel(1, "Rua A, 100", "Casa", 300000.0, "Disponivel", proprietario1, corretor1)
imovel2 = Imovel(2, "Rua A, 100", "Casa", 600000.0, "Disponivel", proprietario2, corretor2)
imovel3 = Imovel(3, "Rua A, 100", "Apartamento", 900000.0, "Disponivel", proprietario1, corretor2)



# ==================================================
# TESTE 1 - Exibir dados dos proprietários
# ==================================================

print("\n" + "=" * 50)
print("TESTE 1 - DADOS DOS PROPRIETÁRIOS")
print("=" * 50)

proprietario1.exibir_dados()
proprietario2.exibir_dados()


# ==================================================
# TESTE 2 - Exibir ficha dos imóveis
# ==================================================

print("\n" + "=" * 50)
print("TESTE 2 - FICHAS DOS IMÓVEIS")
print("=" * 50)

imovel1.exibir_ficha()
imovel2.exibir_ficha()
imovel3.exibir_ficha()


# ==================================================
# TESTE 3 - Alterar status para Alugado
# ==================================================

print("\n" + "=" * 50)
print("TESTE 3 - ALTERAÇÃO DE STATUS")
print("=" * 50)

imovel2.alterar_status("Alugado")
imovel2.exibir_ficha()


# ==================================================
# TESTE 4 - Testar status inválido
# ==================================================

print("\n" + "=" * 50)
print("TESTE 4 - STATUS INVÁLIDO")
print("=" * 50)

imovel3.alterar_status("Reservado")
imovel3.exibir_ficha()


# ==================================================
# TESTE 5 - Alterar status para Disponível
# ==================================================

print("\n" + "=" * 50)
print("TESTE 5 - VOLTAR PARA DISPONÍVEL")
print("=" * 50)

imovel2.alterar_status("Disponivel")
imovel2.exibir_ficha()


# ==================================================
# TESTE 6 - Trocar proprietário
# ==================================================

print("\n" + "=" * 50)
print("TESTE 6 - TROCA DE PROPRIETÁRIO")
print("=" * 50)

resultado = imovel3.alterar_proprietario(proprietario2)

if resultado:
    print("Proprietário alterado com sucesso!")
else:
    print("Não foi possível alterar o proprietário.")

imovel3.exibir_ficha()


# ==================================================
# TESTE 7 - Tentar alterar com proprietário inválido
# ==================================================

print("\n" + "=" * 50)
print("TESTE 7 - PROPRIETÁRIO INVÁLIDO")
print("=" * 50)

resultado = imovel3.alterar_proprietario(None)

if resultado:
    print("Proprietário alterado com sucesso!")
else:
    print("Não foi possível alterar o proprietário.")

imovel3.exibir_ficha()


# ==================================================
# TESTE 8 - Vender imóvel com corretor 1
# ==================================================

print("\n" + "=" * 50)
print("TESTE 8 - VENDA COM CORRETOR 1")
print("=" * 50)

corretor1.vender_imovel(imovel1, proprietario2)


# ==================================================
# TESTE 9 - Verificar imóvel após a venda
# ==================================================

print("\n" + "=" * 50)
print("TESTE 9 - CONFERIR VENDA")
print("=" * 50)

imovel1.exibir_ficha()


# ==================================================
# TESTE 10 - Tentar vender imóvel já vendido
# ==================================================

print("\n" + "=" * 50)
print("TESTE 10 - SEGUNDA VENDA")
print("=" * 50)

corretor1.vender_imovel(imovel1, proprietario1)


# ==================================================
# TESTE 11 - Venda com corretor 2
# ==================================================

print("\n" + "=" * 50)
print("TESTE 11 - VENDA COM CORRETOR 2")
print("=" * 50)

corretor2.vender_imovel(imovel3, proprietario1)


# ==================================================
# TESTE 12 - Conferir todas as fichas ao final
# ==================================================

print("\n" + "=" * 50)
print("TESTE 12 - RELATÓRIO FINAL DOS IMÓVEIS")
print("=" * 50)

imovel1.exibir_ficha()
imovel2.exibir_ficha()
imovel3.exibir_ficha()