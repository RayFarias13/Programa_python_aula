class autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor



class biblioteca2:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        livro = {'titulo': titulo, 'autor': autor}
        self.livros.append(livro)

    
    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro['titulo'] == titulo:
                return livro
        return None
    

    def criarlivro(self, titulo, ano, autor):
        livro = Livro(titulo, ano, autor)
        self.livros.append(livro)
        return livro
    
    def listar_livros(self):
        print(f"Livros disponiveis na biblioteca:")
        for livro in self.livros:
            print(f" - {livro.titulo} ({livro.ano}), Autor: {livro.autor.nome}")
    

class usuario:
    def __init__(self, nome,biblioteca2):
        self.nome = nome
        self.biblioteca2 = biblioteca2
        self.livros_emprestados = []


    def pegar_emprestado(self, Livro):
        if Livro in self.biblioteca2.livros:
            print(f"{self.nome} pegou emprestado o livro '{Livro.titulo}'.")
            self.livros_emprestados.append(Livro)
            self.biblioteca2.livros.remove(Livro)
        else:
            print(f"O livro '{Livro.titulo}' não está disponível na biblioteca.")





def main():
    autor1 = autor("George Orwell", "Britânico")
    autor2 = autor("J.K. Rowling", "Britânica")
    autor3 = autor("Machado de Assis", "Brasileiro")

    biblioteca = biblioteca2()

    livro1 = biblioteca.criarlivro("1984", 1949, autor1)
    livro2 = biblioteca.criarlivro("Harry Potter e a Pedra Filosofal", 1997, autor2)
    livro3 = biblioteca.criarlivro("Dom Casmurro", 1899, autor3)

    biblioteca.listar_livros()


    usuario1 = usuario("Alice", biblioteca)
    usuario2 = usuario("Bob", biblioteca)

    usuario1.pegar_emprestado(livro1)
    usuario2.pegar_emprestado(Livro("Livro Não Existente", 2020, autor3)) 
    ####
    print(f"\nLivros após empréstimos:")
    print(f"{usuario1.nome} tem os seguintes livros emprestados:")
    for livro in usuario1.livros_emprestados:
        print(f" - {livro.titulo} ({livro.ano}), Autor: {livro.autor.nome}")

    if __name__ == "__main__":
        main()