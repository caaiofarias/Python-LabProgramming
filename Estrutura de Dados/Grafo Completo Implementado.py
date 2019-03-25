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

# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i][2] < arr[l][2]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest][2] < arr[r][2]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

class Vertex:#Vertice com valores 

    def __init__(self,nome):
        self.nome = nome
        self.vizinhos = set()
        self.distance = float("inf")
        self.pai = None
        self.visitado = False
    def getVertex(self):
        return self.nome


class Graph:

    def __init__(self):
        self.vertexes = []#lista para os vertices
        self.edges = {}#Dicionario para as arestas
        self.edgesL = []
        self.nomeVertexes = {}#nome dos vertices para cada vertice correspondente
        self.conjVertexes = []
    def addVertex(self,v):
        self.vertexes.append(v)
        self.nomeVertexes[v.getVertex()] = v

    def addEdgeDic(self,v1,v2,peso):#Adicionando aresta para um grafo nao direcionado
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

    def addEdgeList(self,v1,v2,peso):#as arestas ficam numa lista, para poder usar o heapsort
        self.edgesL.append([v1.getVertex(),v2.getVertex(),peso])
        #self.edgesL.append([v2.getVertex(),v1.getVertex(),peso])

    def isEmpty(self,v1,v2):
        try:
            if len(self.edges[v1.getVertex()]) == 1:
                return True
        except:
            return False
    
    def find(self,parent,i):#função para achar o pai
        if parent[i-1] == i:
            return i
        return self.find(parent,parent[i-1])
    def union(self,parent,rank,x,y):#uniao entre 2 conjuntos
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)
        if rank[xroot-1] < rank[yroot-1]:
            parent[xroot-1] = yroot
        elif rank[xroot-1] > rank[yroot-1]:
            parent[yroot-1] = xroot
        else:
            parent[yroot-1] = xroot
            rank[xroot-1] += 1

            
def Menor(Q):#retorna menor distancia no conjunto Q
    menor = float("inf")
    vertice = None
    for i in Q:
        if i.distance < menor:
            menor = i.distance
            vertice = i
    return vertice

def GetVertex(g,valor):
    for i in g.vertexes:
        if valor == i.getVertex():
            return i

def Dijkstra(g,s):#aqui eu passo o grafo e um valor(int) do grafo inicial
    Q = set()
    for i in g.vertexes:
        i.distance = float("inf") 
    g.vertexes[g.nomeVertexes[s].getVertex()].distance = 0#seto a distancia do vertice inicial para 0(as demais ja estao em infinito)
    for i in g.vertexes:
        Q.add(i)
    print(Q)
    while Q != set():
        u = Menor(Q)#pego o vertice com menor distancia
        print(u.getVertex())
        Q.remove(u)
        for viz in u.vizinhos:
            if u.distance + g.edges[u.getVertex()][viz.getVertex()] < viz.distance:#se a distancia do menor + o peso da aresta for < que a dist do vizinho
                viz.distance = u.distance + g.edges[u.getVertex()][viz.getVertex()] # a distancia do vizinho vai ser a nova menor distancia
    return [x.distance for x in g.vertexes]

def kruskal(g):#algoritmo que pega os menores pesos de uma aresta ordenada e cria a menor arvore(caminhos sem ciclos). Algoritmo guloso
    result = []
    parent = [] ; rank = []#criando o "conjunto" pai, e o rank dele
    i,e = 0,0
    heapSort(g.edgesL)
    for node in g.vertexes:
        parent.append(node.getVertex())
        rank.append(0)
    while e < len(g.vertexes)-1:#para cada aresta, se ela nao formar ciclos, add ela no resultado e faz a uniao da aresta (u,v) w é o peso
        u,v,w = g.edgesL[i]
        i+= 1
        x = g.find(parent,u)
        y = g.find(parent,v)
        if x != y:
            e = e+1
            result.append([u,v,w])
            g.union(parent,rank,x,y)
    return result # LEMBRAR QUE OS INDICES DAS FUNÇÕES FIND() E UNION() ESTÃO COM -1, POIS OS VERTICES COMEÇAM EM 1 ATE N-1
'''
Kruskal
1 cria um conjunto A contendo as arestas do grafo
2 while o conjunto A nao for vazio e a floresta n for geradora,
  remove a aresta de menor peso do conj A. Se a aresta removida conecta
  2 arestas, add a floresta e combina a arvores
3 testa se a aresta add ao conjunto a forma um ciclo
'''

def prim(g,s):#recebe o grafo e o nome do vertice de origem
    global Q
    Q = MinHeap() # conj de menores distancias e o indice do vertice
    a,b = [],[] # a é lista de vertices, e b lista pai[u]
    for i in g.vertexes:#for para relaxar os vertices
        i.distance = float("inf")
        i.pai= None
    g.vertexes[s].distance = 0#vertice inicial com distancia 0
    for i in g.vertexes:
        Q.push((i.distance,i.getVertex()))#add a distancia e o nome do vertice na fila
    while Q.isEmpty() == False:#enquanto a heap nao estiver vazia
        u = Q.pop()#tiro o elemento com menor distancia
        if g.vertexes[u[1]].pai != None and u not in b:#se o pai do vertice nao for None quer dizer que ja foi visitado. a outra condição é para evitar repetições na lista
            a.append(g.vertexes[u[1]].pai)# adiciono os pais 
            b.append(u)#adiciono a distancia e o vertice correspondente a ele 
        for viz in g.vertexes[u[1]].vizinhos:#para cada viz de u se ele nao tiver no conj A e o peso de u -> v for < que a distancia da aresta
            if viz.getVertex() not in a and g.edges[u[1]][viz.getVertex()] < viz.distance:
                viz.pai = u[1]#o pai dele é u
                viz.distance = g.edges[u[1]][viz.getVertex()]# e a nova distancia é a menor
                Q = MinHeap([(x.distance,x.getVertex()) for x in g.vertexes])#atualizando as distancias na heap
                Q.heap.remove(u)#removendo u da heap novamente
    return a,b
lista = []
def DFS(g,atual,chegada,anterior,contador):#busca em profundidade recursivo
    global lista#lista para guardar os anteriores ao vertice de destino
    if anterior not in lista and anterior != None:
        lista.append(anterior)
    if atual.getVertex() == chegada.getVertex():
        print(contador)
    else:
        for j in atual.vizinhos:
            if j!= anterior:
                DFS(g,j,chegada,atual,contador+1)#j vira o atual,atual vira o anterior

while True:
        
    c = 1
    entrada = [int(x) for x in input().split()]
    if entrada == [0,0]:
        break
    g = Graph()
    for i in range(1,entrada[0]+1):
        g.addVertex(Vertex(i))
    for j in range(entrada[1]):
        aresta = [int(x) for x in input().split()]
        g.addEdgeList(g.vertexes[aresta[0]-1],g.vertexes[aresta[1]-1],aresta[2])

    x = kruskal(g)

    print("Teste %d" %c)
    aux = 0
    print(x)
    for i in x:
        aux = 0
        print(min(i[aux:len(x)]),max(i[aux:len(x)]))
        aux += 1

    


