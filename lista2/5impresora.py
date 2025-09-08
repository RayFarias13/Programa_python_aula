class impressora:
    def imprimir(self, documento):
        print(documento)

class documento:
    
    def __init__(self, conteudo, titulo):
        self.conteudo = conteudo
        self.titulo = titulo

    def criar_documento(self):
        documento = f"Título: {self.titulo}\nConteúdo: {self.conteudo}"
        return documento

    def listar_documento(self):
        print(f"Título: {self.titulo}\nConteúdo: {self.conteudo}\n")
    

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
            documento_criado = doc.criar_documento()
            documentos.append(doc)
            print("\nDocumento criado com sucesso!")


        elif escolha == "2":
            print("\nDocumentos Criados:")
            for doc in documentos:
                doc.listar_documento()

        elif escolha == "3":
            print("\nDocumentos disponíveis para impressão:")
            for i, doc in enumerate(documentos):
                print(f"{i + 1}. {doc.titulo}")
            escolha_imp = input("\nEscolha o número do documento para imprimir: ")
            if escolha_imp.isdigit() and 1 <= int(escolha_imp) <= len(documentos):
                doc_escolhido = documentos[int(escolha_imp) - 1]
                impressora1 = impressora()
                impressora1.imprimir(doc_escolhido.criar_documento())
            
                
        elif escolha == "4":
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")




if __name__ == "__main__":
    main()