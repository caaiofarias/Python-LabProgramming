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
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] >self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] > self.heap[right]:
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
        self.distance = [float("inf"),float("inf")]
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
            if len(self.edges[v1.getVertex()]) != 0:
                return True
        except:
            return False

def GetVertex(g,valor):
    for i in g.vertexes:
        if valor == i.getVertex():
            return i

def Dijkstra(g,s,c):#aqui eu passo o grafo e 2 valores(int) do grafo inicial,e o final
    Q = MinHeap()
    for i in g.vertexes:#relaxamento dos vertices
        i.distance = [float("inf"),float("inf")]#dist 1 é par dist 2 é pro impar
    g.vertexes[g.nomeVertexes[s].getVertex()-1].distance = [0,float("inf")]#par como infito ???
    for i in g.vertexes:
        Q.push((i.distance,i.getVertex()))#adicionando os vertices no conjunto, e a distancia
    while Q.isEmpty() != True:
        u = Q.pop()#pego o vertice com menor distancia, u[0] é a dist, e, u[1] é o vertice
        if g.vertexes[u[1]-1] == c:#para quando chega na cidade c de destino
            break
        for viz in g.vertexes[u[1]-1].vizinhos:
            if u[0][1] + g.edges[u[1]][viz.getVertex()] < viz.distance[0]:#se a distancia impar + o peso da aresta < distancia par do viz
                viz.distance[0] = u[0][1] + g.edges[u[1]][viz.getVertex()]#a nova distancia par é a distancia impar + peso
                Q.push(u)#coloco no conjunto novamente
            if u[0][0] + g.edges[u[1]][viz.getVertex()] < viz.distance[1]:#se a dist par + o peso da aresta < dist impar do viz
                viz.distance[1] = u[0][0] + g.edges[u[1]][viz.getVertex()]#a nova dist impar é a dist par + peso
                Q.push(u)#coloco novamente
    if g.vertexes[g.nomeVertexes[c.getVertex()].getVertex()-1].distance[0] == float("inf"):#se for inf, não tem caminho par
        print(-1)
    else:
        print(g.vertexes[g.nomeVertexes[c.getVertex()].getVertex()-1].distance[0])#imprimo o caminho par 

g = Graph()
entrada = [int(x) for x in input().split()]
for i in range(1,entrada[0]+1):
    g.addVertex(Vertex(i))#adiciono os vertices
for i in range(1,entrada[1]+1):#adiciono as arestas
    caminho = [int(x) for x in input().split()]
    g.addEdge(GetVertex(g,caminho[0]),GetVertex(g,caminho[1]),caminho[2])
Dijkstra(g,1,g.vertexes[entrada[0]-1])#chama o dijkstra modificado
