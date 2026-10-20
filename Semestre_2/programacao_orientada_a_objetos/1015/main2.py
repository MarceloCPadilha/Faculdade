class Livro:
    def __init__(self, __titulo, __autor, __ano, __paginas):
        self.__titulo = __titulo
        self.__autor = __autor
        self.__ano = __ano
        self.__paginas = __paginas
    
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor
    
    def get_ano(self):
        return self.ano
    
    def get_paginas(self):
        return self.__paginas
        
    def mostrar_informacoes(self):
        print("Titulo: {}".format(self.__titulo))
        print("Autor: {}".format(self.__autor))
        print("Ano: {}".format(self.__ano))
        print("Páginas: {}".format(self.__paginas))

    def set_Titulo(self, novoTitulo):
        if novoTitulo:
            self.titulo = novoTitulo
        else:
            print("Título não pode ser vazio.")

 
livro = Livro("O Ladrão de Raios", "Rick Riordan", 2005, 400)
livro.mostrar_informacoes()
novoTitulo=None
# sendo privado não ocorre erro, mas não altera o valor
livro.__titulo = novoTitulo
livro.mostrar_informacoes()

livro.set_Titulo(novoTitulo)
livro.mostrar_informacoes()

print("Titulo:", livro.__titulo)
print("Titulo get:", livro.get_titulo())