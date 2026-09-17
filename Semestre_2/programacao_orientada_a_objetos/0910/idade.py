import tkinter as tk
from tkinter import messagebox

def retorna_status_idade(idade):
    if idade < 18:
        return "menor de idade"
    elif idade >= 18 and idade <= 60:
        return "maior de idade"
    else:
        return "idoso"


def cadastrar_idade():
    idade = int(entry_idade.get()) # pega o idade
    if idade: # verifica se os campos não estão vazios
        messagebox.showinfo("Status", "Você é {}".format(retorna_status_idade(idade)))
        # Limpa os campos
        limpar_campos()
    else:
        messagebox.showinfo("Preencha os dois campos", "Preencha os dois campos.")


def limpar_campos():
    entry_idade.delete(0, tk.END)


# 1. Cria Janela Principal
janela = tk.Tk()
janela.title("Formulário de Idade")
janela.geometry("350x200")

# Widgets do Formulário
# Label e Entry para o idade
label_idade = tk.Label(janela, text="Idade:")
label_idade.grid(row = 0, column = 0, padx = 0, pady = 10)
label_idade = tk.Entry(janela, width = 30)
entry_idade = tk.Entry(janela, width = 30)
entry_idade.grid(row = 0, column = 1, padx = 0, pady = 10)

# Botões
botao_cadastrar = tk.Button(janela, text = "Mostrar status", command = cadastrar_idade)
botao_cadastrar.grid(row = 2, column = 0, columnspan = 1, padx = 30, pady = 20)
botao_limpar = tk.Button(janela, text = "Limpar", command = limpar_campos)
botao_limpar.grid(row = 2, column = 1, columnspan = 1, pady = 20)

janela.mainloop()
