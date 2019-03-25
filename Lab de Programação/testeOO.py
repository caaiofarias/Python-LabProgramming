class Mamifero(object):
    def __init__(self,especie,nome,cor,idade):
        self.especie = especie
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def GetEspecie(self):
        return self.especie


class Humano(Mamifero):
    def __init__(self,nome,cor,idade):
        super().__init__(self,nome,cor,idade,genero)
        self.especie = "Humano"

class Homem(Humano):
    def __init__(self,nome,cor,idade):
        super(Humano,self).__init__(self,nome,cor,idade)
        self.genero = "Masculino"
