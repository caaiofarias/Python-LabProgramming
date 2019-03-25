class Vertex:#Vertice com valores 

    def __init__(self,nome):
        self.nome = nome
        self.vizinhos = set()
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
    menor = [float("inf"),float("inf")]
    vertice = None
    for i in Q:
        if float('inf') in i.distance:
            if i.distance < menor:
                menor = i.distance
                vertice = i
        else:
            if i.distance[0] + i.distance[1] < menor[0] + menor[1]:
                menor = i.distance
                vertice = i
    return vertice

def Dijkstra(g,s,c):#aqui eu passo o grafo e um valor(int) do grafo inicial
    Q = set()
    for i in g.vertexes:
        i.distance = [float("inf"),float("inf")]
    g.vertexes[g.nomeVertexes[s].getVertex()-1].distance = [0,float("inf")]#par como infito ???
    for i in g.vertexes:
        Q.add(i)#adicionando os vertices no conjunto
    while Q != set():
        print(Q)
        u = Menor(Q)#pego o vertice com menor distancia  
        Q.remove(u)#tiro do conjunto
        if u.distance[0] > u.distance[1] and u.distance[1] > u.distance[0]:
            continue
        if u == c:
            break
        for viz in u.vizinhos:
            if u.distance[1] + g.edges[u.getVertex()][viz.getVertex()] < viz.distance[0]:#se a distancia impar + o peso da aresta < distancia par do viz
                viz.distance[0] = u.distance[1] + g.edges[u.getVertex()][viz.getVertex()]#a nova distancia par é a distancia impar + peso
                Q.add(u)#coloco no conjunto novamente
            if u.distance[0] + g.edges[u.getVertex()][viz.getVertex()] < viz.distance[1]:#se a dist par + o peso da aresta < dist impar do viz
                viz.distance[1] = u.distance[0] + g.edges[u.getVertex()][viz.getVertex()]#a nova dist impar é a dist par + peso
                Q.add(u)#coloco novamente
    if g.vertexes[g.nomeVertexes[c.getVertex()].getVertex()-1].distance[0] == float("inf"):#se for inf, não tem caminho par
        print(-1)
    else:
        print(g.vertexes[g.nomeVertexes[c.getVertex()].getVertex()-1].distance[0])#imprimo o caminho par 

g = Graph()
entrada = [int(x) for x in input().split()]
for i in range(1,entrada[0]+1):
    g.addVertex(Vertex(i))
for i in range(1,entrada[1]+1):
    caminho = [int(x) for x in input().split()]
    g.addEdge(GetVertex(g,caminho[0]),GetVertex(g,caminho[1]),caminho[2])
Dijkstra(g,1,g.vertexes[entrada[0]-1])
