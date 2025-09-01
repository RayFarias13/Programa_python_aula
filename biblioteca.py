class livro:
    def __init__(self, titulo, autor, id_livro):
        self.__titulo = titulo
        self.__autor = autor
        self.__id_livro = id_livro

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_id_livro(self):
        return self.__id_livro
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_id_livro(self, id_livro):
        self.__id_livro = id_livro


class usuario:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula


    def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)
        print(f"{self.__nome} pegou emprestado o livro '{livro.get_titulo()}'.\n")

    def devolver_livro(self, id_livro):
        for livro in self.__livros_emprestados:
            if livro.get_id_livro() == id_livro:
                self.__livros_emprestados.remove(livro)
                print(f"{self.__nome} devolveu o livro '{livro.get_titulo()}'.\n")
                return
        print(f"\n{self.__nome} não tem o livro com ID {id_livro} emprestado.\n")

    def listar_livros_emprestados(self):
        if not self.__livros_emprestados:
            print(f"{self.__nome} não tem livros emprestados.\n")
            return
        else:  
            print (f"Livros emprestados por {self.__nome}:")
            for livro in self.__livros_emprestados:
                print(f"- {livro.get_titulo()} (ID: {livro.get_id_livro()})\n")




def main():
    livro1 = livro ("Harry Potter","J. K. Rolling",1)
    livro2 = livro ("Jogos Vorazes","Suzanne Collins",2)
    livro3 = livro ("Dom Casmurro","Machado de Assis",3)


    usuario1 = usuario ("Marcos", 111111)


    usuario1.emprestar_livro(livro1)
    usuario1.emprestar_livro(livro2)
    

    usuario1.listar_livros_emprestados()

    usuario1.devolver_livro(2)

    usuario1.listar_livros_emprestados()


if __name__ == "__main__":
    main()