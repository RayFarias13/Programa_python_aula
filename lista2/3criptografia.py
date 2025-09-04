class criptografia:
    def __init__(self, texto):
        self.texto = texto

    def criptografar(self):
        texto_criptografado = []
        for i in range(len(self.texto)):
            if self.texto.upper()[i] == "A":
                texto_criptografado.append("4")
            elif self.texto.upper()[i] == "E":
                texto_criptografado.append("3")
            elif self.texto.upper()[i] == "I":
                texto_criptografado.append("1")
            elif self.texto.upper()[i] == "O":
                texto_criptografado.append("0")
            elif self.texto.upper()[i] == "U":
                texto_criptografado.append("8")
            else:
                texto_criptografado.append(self.texto[i])
        return "".join(texto_criptografado)

def main():
    texto = input("Digite um texto para criptografar: ")
    cript = criptografia(texto)
    resultado = cript.criptografar()
    print("Texto criptografado:", resultado)



if __name__ == "__main__":
    main()   


