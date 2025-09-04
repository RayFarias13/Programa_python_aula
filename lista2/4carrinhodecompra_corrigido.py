# Carrinho de Compra com erros

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
        if nome != "":
            self.__nome = nome
        else:
            print("Nome inválido.")

    def set_preco(self,preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço inválido.")

    def set_quantidade(self,quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            print("Quantidade inválida.")

    def calcular_total(self):
        return self.__preco * self.__quantidade


class carrinhodecompra:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.get_nome().lower() == nome.lower():
                self.produtos.remove(produto)
                return True

        return False

    def listar_produtos(self):
        if not self.produtos:
            print("\nCarrinho vazio.")
            return 
        else:
            print("\nProdutos no carrinho:")
            for produto in self.produtos:
                print(f"Nome: {produto.get_nome()}, Preço unitario: {produto.get_preco()}, Quantidade: {produto.get_quantidade()}, Total: {produto.calcular_total()}")
        
    
    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.calcular_total()
        return total
    


def main():
    carrinho = carrinhodecompra()
    while True:
        print("\nMenu do carrinho:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Calcular total")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("\nNome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            nproduto = produto(nome, preco, quantidade)
            carrinho.adicionar_produto(nproduto)
            print(f"Produto '{nome}' adicionado com sucesso.")

        elif opcao == "2":
            nome = input("\nNome do produto a ser removido: ")
            for produto in carrinho.produtos:
                print (produto.get_nome())

            if carrinho.remover_produto(nome):
                print(f"Produto '{nome}' removido com sucesso.")
            else:
                print(f"Produto '{nome}' não encontrado no carrinho.")

        elif opcao == "3":
            carrinho.listar_produtos()
        
        elif opcao == "4":
            total = carrinho.calcular_total()
            print(f"\nTotal do carrinho: {total}")



#if __name__ == "__main__":
main()