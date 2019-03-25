class Vertex:#Vertice com valores 

    def __init__(self,nome):
        self.nome = nome
        self.vizinhos = set()
        self.visitado = False
        self.distance = float("inf")
    def getVertex(self):
        return self.nome


class Graph:

    def __init__(self):
        self.vertexes = []#lista para os vertices
        self.edges = {}#Dicionario para as arestas
        self.nomeVertexes = {}#nome dos vertices para cada vertice correspondente
    def addVertex(self,v):
        self.vertexes.append(v)
        self.nomeVertexes[v.getVertex()] = v

    def addEdge(self,v1,v2,peso):#Adicionando aresta para um grafo nao direcionado
        if self.isEmpty(v1,v2)== False:#verifica se o grafo esta vazio, se sim entra no if, caso nao esteja entra no else dando update de a -> b
            self.edges[v1.getVertex()] = {}#cria o valor para a chave
            self.edges[v1.getVertex()] = {v2.getVertex():peso}#add uma chave no valor do vertice{o destino e o peso}

        else:
            self.edges[v1.getVertex()].update({v2.getVertex():peso})
        if self.isEmpty(v2,v1)== False:#aqui faço a mesma coisa só que a volta do caminho. de b -> a
            self.edges[v2.getVertex()] = {}
            self.edges[v2.getVertex()] = {v1.getVertex():peso}
        else:
            self.edges[v2.getVertex()].update({v1.getVertex():peso})

        v1.vizinhos.add(v2)
        v2.vizinhos.add(v1)

    def isEmpty(self,v1,v2):
        try:
            if len(self.edges[v1.getVertex()]) != 0:
                return True
        except:
            return False

def GetVertex(g,valor):
    for i in g.vertexes:
        if valor == i.getVertex():
            return i

def Menor(Q):#retorna menor distancia no conjunto Q
    menor = float("inf")
    vertice = None
    for i in Q:
        if i.distance < menor:
            menor = i.distance
            vertice = i
    return vertice

def Dijkstra(g,s):#aqui eu passo o grafo e um valor(int) do grafo inicial
    Q = set()
    for i in g.vertexes:
        i.distance = float("inf") 
    g.vertexes[g.nomeVertexes[s].getVertex()-1].distance = 0#seto a distancia do vertice inicial para 0(as demais ja estao em infinito)
    for i in g.vertexes:
        Q.add(i)
    while Q != set():
        u = Menor(Q)#pego o vertice com menor distancia
        Q.remove(u)
        for viz in u.vizinhos:
            if u.distance + g.edges[u.getVertex()][viz.getVertex()] < viz.distance:#se a distancia do menor + o peso da aresta for < que a dist do vizinho
                viz.distance = u.distance + g.edges[u.getVertex()][viz.getVertex()] # a distancia do vizinho vai ser a nova menor distancia
    return [x.distance for x in g.vertexes]


c = 1
while True:
    res1 = []
    g = Graph()
    entrada = int(input())
    if entrada == 0:
        break
    for i in range(1,entrada+1):
        g.addVertex(Vertex(i))
    for i in range(entrada-1):
        caminho = [int(x) for x in input().split()]
        g.addEdge(GetVertex(g,caminho[0]),GetVertex(g,caminho[1]),1)
    for i in range(1,entrada+1):
        res = Dijkstra(g,i)
        if float("inf") in res:
            res.remove(float("inf"))
        res1.append((max(res),i))
    print("Teste %d"%(c))
    print(min(res1)[1])
    print()
    c+=1
