import tkinter as tk
from tkinter import messagebox

def classificar_imc(imc):
    # Classificação baseada na tabela
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25.0:
        classificacao = "Peso normal"
    elif 25.0 <= imc < 30.0:
        classificacao = "Sobrepeso"
    elif 30.0 <= imc < 35.0:
        classificacao = "Obesidade Grau I"
    elif 35.0 <= imc < 40.0:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III (Mórbida)"
        
    return classificacao

def calculo_de_imc(peso, altura):
    return peso / (altura * altura)

def limpar_campos():
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)

def calcular_imc():
    peso = entry_peso.get().strip().replace(",", ".") # pega o altura
    altura = entry_altura.get().strip().replace(",", ".") # pega a altura
    if peso and altura: # verifica se os campos não estão vazios
        altura = float(altura)
        peso = float(peso)
        if peso <= 0 or altura <= 0:
            messagebox.showinfo("Os valores devem ser números positivos", "Os dois valores devem ser números positivos")

        messagebox.showinfo("Cadastro Realizado", "Peso: {}\naltura: {}\n\nIMC: {}\nClassificação: {}".format(peso, altura, calculo_de_imc(peso, altura), classificar_imc(calculo_de_imc(peso, altura))))
        # Limpa os campos
        limpar_campos()
    else:
        messagebox.showinfo("Preencha os dois campos", "Preencha os dois campos.")


# 1. Cria Janela Principal
janela = tk.Tk()
janela.title("Caculadora de IMC")
janela.geometry("400x200")

# Widgets do Formulário
# Label e Entry para a Altura
label_altura = tk.Label(janela, text="Altura(m|ex. 1.75):")
label_altura.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
label_altura = tk.Entry(janela, width = 30)
entry_altura = tk.Entry(janela, width = 30)
entry_altura.grid(row = 0, column = 1, padx = 10, pady = 10)

# Label e Entry para a altura
label_peso = tk.Label(janela, text="Peso(kg|ex. 70.5):")
label_peso.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
label_peso = tk.Entry(janela, width = 30)
entry_peso = tk.Entry(janela, width = 30)
entry_peso.grid(row = 1, column = 1, padx = 10, pady = 10)

# Botões
botao_calcular = tk.Button(janela, text = "Calcular", command = calcular_imc)
botao_calcular.grid(row = 2, column = 0, columnspan = 1, padx = 30, pady = 20)
botao_limpar = tk.Button(janela, text = "Limpar", command = limpar_campos)
botao_limpar.grid(row = 2, column = 1, columnspan = 1, pady = 20)

janela.mainloop()
