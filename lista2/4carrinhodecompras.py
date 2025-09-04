#bug no novo_produto = produto(nome, preco, quantidade)

class produto:
    def __init__(self,nome,preco,quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_nome(self,nome):
        self.__nome = nome

    def set_preco(self,preco):
        self.__preco = preco

    def set_quantidade(self,quantidade):
        self.__quantidade = quantidade

class carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self,produto):
        self.produtos.append(produto)
            
    def remover_produto(self,nome):
        for produto in self.produtos:
            if produto.get_nome() == nome:
                self.produtos.remove(produto)
                return True
        return False

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total
    

def main():
    carrinho_compras = carrinho()

    while True:
        print("\n1. Adicionar produto")
        print("2. Remover produto")
        print("3. Ver total")
        print("4. Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            if preco < 0:
                print("Preço inválido. Tente novamente.")
                continue

            quantidade = int(input("Quantidade do produto: "))
            if quantidade < 0:
                print("Quantidade inválida. Tente novamente.")
                continue

            novo_produto = produto(nome, preco, quantidade)
            carrinho_compras.adicionar_produto(novo_produto)
            print(f"Produto {nome} adicionado ao carrinho.")
        elif escolha == "2":
            if not carrinho_compras.produtos:
                print("O carrinho está vazio.")
            else:
                for produto in carrinho_compras.produtos:
                        print(f"Produto: {produto.get_nome()}, Preço: R$ {produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")
                        total = carrinho_compras.calcular_total()
                nome = input("Nome do produto a remover: ")

                if carrinho_compras.remover_produto(nome):
                    print(f"Produto {nome} removido do carrinho.")
                else:
                    print(f"Produto {nome} não encontrado no carrinho.")
        elif escolha == "3":
            if not carrinho_compras.produtos:
                print("O carrinho está vazio.")
            else:
                for produto in carrinho_compras.produtos:
                    print(f"Produto: {produto.get_nome()}, Preço: R$ {produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")
                total = carrinho_compras.calcular_total()
                print(f"Total do carrinho: R$ {total:.2f}")
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()