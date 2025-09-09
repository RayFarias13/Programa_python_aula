class Casa:
    class __comodo:
        def __init__(self, nome, area):
            self.__nome = nome
            self.__area = area

        def get_nome(self):
            return self.__nome
        
        def get_area(self):
            return self.__area
        


    def __init__(self):
        self.__comodos = []

    def adicionar_comodo(self, nome, area):
        comodo = self.__comodo(nome, area)
        self.__comodos.append(comodo)


    def listar_comodos(self):
        if not self.__comodos:
            print("\nNenhum cômodo adicionado.\n")
        else:
            print("\nCômodos da casa:")
            for comodo in self.__comodos:
                print(f"\n- Cômodo: {comodo.get_nome()}, Área: {comodo.get_area()} m²")


    def calcular_area_total(self):
        total = 0
        for comodo in self.__comodos:
            total += comodo.get_area()
        return total

def main():
    while True:
        print("Menu:")
        print("1. criar casa")
        print("2. Adicionar cômodo")
        print("3. Listar cômodos")
        print("4. Calcular área total")
        print("5. Sair")


        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            casa = Casa()
            print("\nCasa criada com sucesso!")

        elif opcao == "2":
            if casa is None:
                print("\Crie uma casa primeiro!")
            else:
                nome = input("Nome do cômodo: ")
                area = float(input("Área do cômodo (m²): "))
                casa.adicionar_comodo(nome, area)
                print(f"Cômodo ({nome}) com área de ({area}) m² adicionado com sucesso!")
        elif opcao == "3":
            if casa is None:
                print("\nCrie uma casa primeiro!")
            else:
                casa.listar_comodos()

        elif opcao == "4":
            if casa is None:
                print("\nCrie uma casa primeiro!")
            else:
                area_total = casa.calcular_area_total()
                print(f"\nÁrea total da casa: {area_total} m²")











if __name__ == "__main__":
    main()