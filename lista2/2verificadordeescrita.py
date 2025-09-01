class analizadorstring:
    def __init__(self, texto):
        self.texto = texto

    def numero_de_caracteres(self):
        return len(self.texto)

    def caracteres(self):
        maiusculo = []
        minusculo = []
        for i, t in enumerate(self.texto):
            if t.isupper():
                maiusculo.append(t)
            else:
                minusculo.append(t)
        return maiusculo, minusculo

def main():
    texto = input("Digite um texto: ")

    verificador = analizadorstring(texto)
    verificador.numero_de_caracteres()

    print("Número de caracteres:", verificador.numero_de_caracteres())
    print("Número de caracteres maiúsculos:", verificador.caracteres()[0])
    print("Número de caracteres minúsculos:", verificador.caracteres()[1])

if __name__ == "__main__":
    main()