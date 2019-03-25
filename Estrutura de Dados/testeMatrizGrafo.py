class Vertice:
    def __init__(self,nome):
        self.nome = nome
        self.visitado = False
    def igual(self,r):
        return r == self.nome
    def foiVisitado(self):
        return self.visitado
    def regVisitado(self):
        self.visitado = True
    def limpa(self):
        self.visitado = False

    def getNome(self):
        return self.nome
class Grafo:
    def __init__(self,numVertice):
        self.numVertice = numVertice
        self.numvertices = 0
        self.listaVertices = []
        self.matrizAdj = []
        for i in range(self.numVertice):
            linhaMatriz = []
            for j in range(self.numVertice):
                linhaMatriz.append(0)
            self.matrizAdj.append(linhaMatriz)
    def addVertice(self,nome):
        self.numVertice+= 1
        self.listaVertices.append(Vertice(nome))

    def AddAresta(self,inicio,fim):
        self.matrizAdj[inicio][fim] = 1
        self.matrizAdj[fim][inicio] = 1

    def mostraVertice(self,vertice):
        print(self.listaVertice[vertice].getNome())

    def imprimeMatriz(self):
        print()

        for i in range(self.numVertice):
            print(self.listaVertices[i].getNome())
        print()
        for i in range(self.numVertice):
            print(self.listaVertices[i].getNome())
            for j in range(self.numVertice):
                print(self.matrizAdj[i][j])
            print()
    def buscaVertice(self,nome):
        for i in range(self.numVertice):
            if self.listaVertices[i].igual(nome):
                return i
            return -1

    def AdjNaoVisitado(self,v):
        for i in range(self.numVertice):
            if self.matrizAdj[v][i] == 1 and self.listaVertices[i].foiVisitado() == False:
                return i
        return -1
    def dfs(self,inicio,fim):
        pilha = []
        self.listaVertices[inicio].regVisitado()
        pilha.append(inicio)
        while len(pilha) != 0:
            elem = pilha[len(pilha)-1]
            if elem == fim:
                print("Encontrado, caminho:")
                for i in pilha: print(self.listaVertice[i].getNome())
                print()
                break
            v = sele.AdjNaoVisitado(elem)
            if v == -1:
                pilha.pop()
            else:
                self.listaVertices[v].regVisitado()
                pilha.append(v)
        else:
            print("N achou caminho")
        for i in self.listaVertices:
            i.limpa()

    def bfs(self,inicio,fim):
        fila = []
        if inicio == fim:
            return
        self.listaVertices[inicio].regVisitado()
        self.buscaVertice(inicio)
        while len(fila) != 0:
            elem = fila.pop(0)

