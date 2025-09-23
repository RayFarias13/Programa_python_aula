from abc import ABC, abstractmethod


class ClubeParticipante(ABC):
    def __init__(self,nome,pais,confederacao,ranking_fifa,golsmarcados,vitorias):
        self.nome=nome
        self.pais = pais
        self.confederacao = confederacao
        self.ranking_fifa = ranking_fifa
        self.golsmarcados = golsmarcados
        self.vitorias = vitorias
        
    def exibir_dados(self):
        print(f"\nClube: {self.nome}")
        print(f"Pais: {self.pais}")
        print(f"Confederaçao: {self.confederacao}")
        print(f"Ranking_Fifaf: {self.ranking_fifa}")
        print(f"Gols Marcados: {self.golsmarcados}")
        print(f"Vitorias: {self.vitorias}")

    @abstractmethod
    def calcular_desepenho(self):
        pass

    abstractmethod
    def gerar_relatorio_tecnico(self):
        pass

class ClubeUEFA(ClubeParticipante):
    def calcular_desepenho(self):
        return (self.vitorias * 3) + (self.golsmarcados * 0.5)
    
    def gerar_relatorio_tecnico(self):
        self.exibir_dados()
        desempenho = self.calcular_desepenho()
        print(f"Desempenho Técnico: {desempenho:.2f}")
    

class ClubeCONMEBOL(ClubeParticipante):
    def calcular_desepenho(self):
        return (self.vitorias * 3) + (self.golsmarcados * 0.7)

    def gerar_relatorio_tecnico(self):
        self.exibir_dados()
        desempenho = self.calcular_desepenho()
        print(f"Desempenho Técnico: {desempenho:.2f}")


        

def main():
    realmadrid = ClubeUEFA("Real Madrid", "Espanha", "UEFA", 1,10,4)
    botafogo = ClubeCONMEBOL("Botafogo","Brasil","Conmebol",5,12,3)


    clubes = [realmadrid,botafogo]


    for clube in clubes:
        print('\n + * 40')
        clube.gerar_relatorio_tecnico()





if __name__ == "__main__":
    main()