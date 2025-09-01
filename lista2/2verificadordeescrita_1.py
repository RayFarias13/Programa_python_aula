class analizadorstring:
    def __init__(self, texto):
        self.texto = texto

    def numero_de_caracteres(self):
        return len(self.texto)

    def caracteres_maiusculos(self):
        return [t for t in self.texto if t.isupper()]

    def caracteres_minusculos(self):
        return [t for t in self.texto if t.islower()]
    

    def contar_vogais(self):
        vogais = 'aeiouAEIOU'
        contador = 0
        for caracter in self.texto:
            if caracter in vogais:
                contador += 1
        return contador
    

    def contemIFB(self):
        return "IFB" in self.texto.upper()
    


def main():
    texto = input("Digite um texto: ")

    verificador = analizadorstring(texto)

    print("Número de caracteres:", verificador.numero_de_caracteres())
    print("Número de caracteres maiúsculos:", verificador.caracteres_maiusculos())
    print("Número de caracteres minúsculos:", verificador.caracteres_minusculos())
    print("Número de vogais:", verificador.contar_vogais())
    if verificador.contemIFB():
        print("Contém 'IFB':", verificador.contemIFB())
    else:
        print("Não contém 'IFB'.")

if __name__ == "__main__":
    main()