class departamento:
    departamentos = []
    def __init__(self, nome, mediasalarial):
        self.nome = nome
        self.mediasalarial = mediasalarial
        self.funcionarios = []

    
    def listar_departamentos(self):
        print("Departamentos:")
        for departamento in self.departamentos:
            print(f"- {departamento.nome}")

    def media_salarial(self):
        if not self.funcionarios:
            return 0
        total_salario = sum(funcionario.cargo.salario for funcionario in self.funcionarios)
        return total_salario / len(self.funcionarios)

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Funcionários do departamento {self.nome}:")
        for funcionario in self.funcionarios:
            print(f"- {funcionario.nome}, Cargo: {funcionario.cargo}")


class funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo



class cargo:
    cargo = ["Analista de RH", 5000,
    "Desenvolvedor", 7000,
    "Vendedor", 4000,
    "Gerente", 9000]
    
    def __init__(self, titulo, salario):
        self.titulo = titulo
        self.salario = salario



def main():
    funcionarios = []
    departamentos1 = []
    
    

    


    while True:
        print("\nMenu:")
        print ("1 - Criar funcionário")
        print ("2 - Criar departamento")
        print ("3 - Adicionar funcionário a um departamento")
        print ("4 - Listar funcionários de um departamento")
        print ("5 - Media salarial de um departamento")
        print ("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do funcionário: ")
            print("Cargos disponíveis:")
            for i, (titulo) in enumerate(cargo.cargo):
                print(f"{i + 1}. {titulo}")
            escolha_cargo = input("Escolha o número do cargo: ")
            if escolha_cargo.isdigit() and 1 <= int(escolha_cargo) <= len(cargo.cargo):
                titulo = cargo.cargo[int(escolha_cargo) - 1]
                novo_cargo = cargo(titulo)
                novo_funcionario = funcionario(nome, novo_cargo)
                funcionarios.append(novo_funcionario)
                print(f"Funcionário {nome} com cargo de {titulo} criado com sucesso.")
            else:
                print("Opção de cargo inválida.")

        elif opcao == "2":
            nome = input("Digite o nome do departamento: ")
            novo_departamento = departamento(nome)
            departamentos1.append(novo_departamento)

        elif opcao == "3":

        




        elif opcao == "4":
            nome_departamento = input("Digite o nome do departamento: ")
            departamento = next((d for d in departamento.departamentos if d.nome == nome_departamento), None)
            if departamento:
                departamento.listar_funcionarios()
            else:
                print("Departamento não encontrado.")

        elif opcao == "5":
            nome_departamento = input("Digite o nome do departamento: ")
            departamento = next((d for d in departamento.departamentos if d.nome == nome_departamento), None)
            if departamento:
                media = departamento.media_salarial()
                if media is not None:
                    print(f"Média salarial do departamento {nome_departamento}: R${media:.2f}")
                else:
                    print("Nenhum funcionário encontrado no departamento.")
            else:
                print("Departamento não encontrado.")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()