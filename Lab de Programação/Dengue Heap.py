class MinHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [-1]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
            
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            min = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            min = self.heap.pop()
        else: 
            min = False
        return min

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index][0] < self.heap[parent][0]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest][0] >self.heap[left][0]:
            largest = left
        if len(self.heap) > right and self.heap[largest][0] > self.heap[right][0]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
    def isEmpty(self):
            if len(self.heap) == 1:
                return True
            return False


class Vertex:#Vertice com valores 

    def __init__(self,nome):
        self.nome = nome
        self.vizinhos = []
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

        v1.vizinhos.append(v2)
        v2.vizinhos.append(v1)

    def isEmpty(self,v1,v2):
        try:
            if len(self.edges[v1.getVertex()]) == 1:
                return True
        except:
            return False

def GetVertex(g,valor):
    for i in g.vertexes:
        if valor == i.getVertex():
            return i

def Dijkstra(g,s):#aqui eu passo o grafo e um valor(int) do grafo inicial
    global Q
    Q = MinHeap()
    for i in g.vertexes:
        i.distance = float("inf") 
    g.vertexes[g.nomeVertexes[s].getVertex()-1].distance = 0#seto a distancia do vertice inicial para 0(as demais ja estao em infinito)
    Q.push((g.vertexes[g.nomeVertexes[s].getVertex()-1].distance,g.vertexes[g.nomeVertexes[s].getVertex()-1]))
    while Q.isEmpty() != True:
        u = Q.pop()#pego o vertice com menor distancia
        for viz in g.vertexes[u[1].getVertex()-1].vizinhos:
            if u[0] + g.edges[u[1].getVertex()][viz.getVertex()] < viz.distance:#se a distancia do menor + o peso da aresta for < que a dist do vizinho
                viz.distance = u[0] + g.edges[u[1].getVertex()][viz.getVertex()] # a distancia do vizinho vai ser a nova menor distancia
                Q.push([viz.distance,viz])
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
