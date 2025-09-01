class ProgressaoAritmetrica:
    def __init__(self, primeiro_termo, razao):
        

        self.primeiro_termo = primeiro_termo
        self.razao = razao

    def calcular_elementos(self, n):
        return self.primeiro_termo + self.razao * (n - 1)

    def calcular_soma_elementos(self, n):
        return n * (self.primeiro_termo + self.calcular_elementos(n)) / 2

    def termos_da_progressao(self, n):
        return [f"Termo: {i}: {self.calcular_elementos(i)}" for i in range(1, n + 1)]


def main():
    primeiro_termo = int(input("\nDigite o primeiro termo da PA: "))
    razao = int(input("\nDigite a razão da PA: "))
    pa = ProgressaoAritmetrica(primeiro_termo, razao)
    n = int(input("\nDigite o número de termos que deseja calcular: "))
    somatermos = pa.calcular_soma_elementos(n)
    print(f"\nA soma dos {n} primeiros termos da PA é: {somatermos}")
    somaelementos = pa.calcular_elementos(n)
    print(f"\nO {n}º termo da PA é: {somaelementos}")
    termos = pa.termos_da_progressao(n)

    print(f"\nOs {n} termos da PA são:")
    for termo in termos:
        print(termo)

if __name__ == "__main__":
    main()
