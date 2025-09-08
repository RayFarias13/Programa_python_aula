from typing import Any


class documento:
    def __init__(self, conteudo, titulo):
        self.__conteudo = conteudo
        self.__titulo = titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_titulo(self):
        return self.__titulo
    
    def set_conteudo(self, conteudo):
        self.__conteudo = conteudo

    def set_titulo(self, titulo):
        self.__titulo = titulo

class impressora:
    def imprimir(self, documento):
        print ("\n==IMPRESAO DE DOCUMENTO==")
        print(f"Título: {documento.get_titulo()}")
        print(f"Conteúdo: {documento.get_conteudo()}")
        print ("============================")



def main():
    documentos = []

    while True:
        print("\nMenu:")
        print("1. Criar Documento") 
        print("2. Listar Documento")
        print("3. Imprimir Documento") 
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            titulo = input("\nDigite o título do documento: ")
            conteudo = input("\nDigite o conteúdo do documento: ")
            doc = documento(conteudo, titulo)
            documentos.append(doc)
            print("\nDocumento criado com sucesso!")


        elif escolha == "2":
            if not documentos:
                print("\nNenhum documento criado.")
                continue

            print("\nDocumentos Criados:")
            for i, doc in enumerate(documentos):
                print(f"{i + 1}. {doc.get_titulo()}")
                
            

        elif escolha == "3":
            print("\nDocumentos disponíveis para impressão:")
            for i, doc in enumerate(documentos):
                print(f"{i + 1}. {doc.get_titulo()}")
            escolha_imp = input("\nEscolha o número do documento para imprimir: ")
            if escolha_imp.isdigit() and 1 <= int(escolha_imp) <= len(documentos):
                doc_escolhido = documentos[int(escolha_imp) - 1]
                impressora1 = impressora()
                impressora1.imprimir(doc_escolhido)
            
                
        elif escolha == "4":
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")



if __name__ == "__main__":
    main()