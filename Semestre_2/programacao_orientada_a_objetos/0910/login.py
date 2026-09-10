import tkinter as tk
from tkinter import messagebox

def cadastrar_usuario():
    usuario = entry_usuario.get() # pega o usuario
    senha = entry_senha.get() # pega a senha
    if usuario and senha: # verifica se os campos não estão vazios
        messagebox.showinfo("Cadastro Realizado", "Usuário: {}\nSenha: {}".format(usuario, senha))
        # Limpa os campos
        limpar_campos()
    else:
        messagebox.showinfo("Preencha os dois campos", "Preencha os dois campos.")


def limpar_campos():
    entry_usuario.delete(0, tk.END)
    entry_senha.delete(0, tk.END)


# 1. Cria Janela Principal
janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("350x200")

# Widgets do Formulário
# Label e Entry para o Usuário
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
label_usuario = tk.Entry(janela, width = 30)
entry_usuario = tk.Entry(janela, width = 30)
entry_usuario.grid(row = 0, column = 1, padx = 10, pady = 10)

# Label e Entry para a Senha
label_senha = tk.Label(janela, text="Senha:")
label_senha.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
label_senha = tk.Entry(janela, width = 30)
entry_senha = tk.Entry(janela, width = 30)
entry_senha.grid(row = 1, column = 1, padx = 10, pady = 10)

# Botão de Cadastro
botao_cadastrar = tk.Button(janela, text = "Cadastrar", command = cadastrar_usuario)
botao_cadastrar.grid(row = 2, column = 0, columnspan = 1, padx = 30, pady = 20)
botao_limpar = tk.Button(janela, text = "Cadastrar", command = limpar_campos)
botao_limpar.grid(row = 2, column = 1, columnspan = 1, pady = 20)

janela.mainloop()
