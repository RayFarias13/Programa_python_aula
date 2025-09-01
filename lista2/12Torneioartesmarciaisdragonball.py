class lutador:
    def __init__(self, nome, poder, nivel):
        self.nome = nome
        self.nivelpoder = poder
    
    def __init_subclass__(self,saiyajin):
        super().__init_subclass__()
        self.saiyajin = saiyajin
