from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,declarative_base
# Configurações do banco de dados
DATABASE_URL ="sqlite:///usuarios.db"
# Criação do engine e da sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Definição do modelo
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    senha=Column(String(50), nullable=False)
    e_mail=Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

# Função para inserir um novo usuário
def insert_Usuario(name, senha, e_mail, age):
    # cria Objeto new_Usuario para inserir no Banco
    new_Usuario = Usuario(name=name,  senha=senha, e_mail=e_mail, age=age)
    #insert into Usuario (name, senha, e_mail, age) values (name, senha, e_mail, age)
    session.add(new_Usuario)
    session.commit()
    print(f'Usuário {name} adicionado com sucesso!')

# Função para atualizar um usuário
def update_Usuario(name):
    usuario = session.query(Usuario).filter_by(name=name).first()
    if usuario:
        new_senha = input('Senha:')
        new_e_mail = input('E-mail:')
        new_age = int(input("Nova idade: "))

        usuario.age = new_age
        usuario.senha=new_senha
        usuario.e_mail=new_e_mail
        session.commit()
        print(f'Usuário {name} atualizado para a idade {new_age}.')
    else:
        print(f'Usuário {name} não encontrado.')

def update_Usuario_id(id):
    print('update usuario por id')

# Função para deletar um usuário
def delete_Usuario(name):
     #busca usuario para Delete
    #select * from Usuario where usuario.name=name
     # first (Trás somente o PRIMEIRO que encontrar na tabela)
    usuario = session.query(Usuario).filter_by(name=name).first()
    # se existir o registro usuario
    if usuario:
        # delete from usuario where usuario.name=name
        session.delete(usuario)
        # confirma no Banco
        session.commit()
        print(f'Usuário {name} deletado com sucesso.')
    else:
        print(f'Usuário {name} não encontrado.')

def delete_Usuario_id(id):
  	print(" deletar por id")

# Função para listar todos os usuários
def list_Usuarios():
    session = Session()
    # select * from Usuario
    # lista TODOS [.all()] Registros da tabela
    all_Usuarios = session.query(Usuario).all()
    if all_Usuarios:
        # para cada registro encontrado desmembra em user...
        for user in all_Usuarios:
            print(f'ID: {user.id}, Nome: {user.name}, senha: {user.senha}, e-mail: {user.e_mail}, Idade: {user.age} ')
    else:
        print('Nenhum usuário encontrado.')

# Função principal para interagir com o usuário
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar usuário")
        print("2. Atualizar usuário")
        print("3. Deletar usuário")
        print("4. Listar usuários")
        print("5. Atualizar usuario por ID")
        print("6. Deletar usuário por ID")
        print("7. Sair")

        choice = input("Opção: ")

        if choice == '1':
            name = input("Nome do usuário: ")
            senha=input('Senha:')
            e_mail=input('E-mail:')
            while True:
                try:
                    age = int(input("Idade do usuário: "))
                    break
                except:
                    print("Digite Idade em INTEIROS")

            insert_Usuario(name, senha, e_mail, age )
        elif choice == '2':
            list_Usuarios()
            name = input("Nome do usuário a ser atualizado(case sensitive): ")
            update_Usuario(name)
        elif choice == '3':
            list_Usuarios()
            name = input("Nome do usuário a ser deletado(case sensitive): ")
            delete_Usuario(name)
        elif choice == '4':
            list_Usuarios()
            input('[Enter] Continua!')
        elif choice == '5':
            list_Usuarios()
            id= int(input('ID do usuario para atualizar:'))
            update_Usuario_id(id)
        elif choice == '6':
            list_Usuarios()
            id = int(input("ID do usuário a ser deletado: "))
            delete_Usuario_id(id)
        elif choice == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Cria a tabela se não existir
    main()
    session.close()
