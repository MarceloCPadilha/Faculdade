import tkinter as tk #importa a biblioteca e a renomeia

#1.cria a janela
janela = tk.Tk()
janela.title("Minha Primeira Janela Tkinter")
janela.geometry("400x300")

janela2=tk.Tk()
janela2.title('pagina auxiliar')
janela2.geometry("400x200")

#2. adiciona um widget(por exemplo um label)
label_boas_vindas=tk.Label(janela,text='ola mundo')
label_boas_vindas.pack(pady=20)
label_local = tk.Label(janela, text="UNISENAC 2026")
label_local.pack(pady=20)
label_nome=tk.Label(janela,text='Fabio')
label_nome.pack(pady=10)

label_auxiliar=tk.Label(janela2, text='auxiliar')
label_auxiliar.pack(pady=10)

#3.inicia o loop principal 
janela.mainloop()
janela2.mainloop()