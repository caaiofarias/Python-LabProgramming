class GrafoLista:
    def __init__(self,num):
        self.nodes = set()#conjunto de vertices
        self.edges = [[]for i in range(num)]#lista de arestas e relações
        self.distances = {}#dic para guardas as distancias, onde a chave é a aresta(u,v)

    def addNodes(self,value):
        self.nodes.add(value)
    def addEdges(self,src,dest,distance):
        self.edges[src].append(dest)
        self.distances[(src,dest)] = distance

  
class GrafoMatriz:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[float("inf")] * vertices for i in range(vertices)]
        self.visitados = [False]* vertices
    def addAresta(self,u,v,peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

#RedeOtica
def Kruskal(Graf):
    AGM = []
    Vertices = []
    Tabas = []

    for x in range(len(Graf)):
        for z in range(len(Graf)):
            dados = []
            if Graf[x][z] != 0:
                dados.append(Graf[x][z]) #Valor da aresta
                dados.append(x+1) #Valor da linha
                dados.append(z+1) #Valor da coluna
                Vertices.append(dados)
    Vertices.sort() #Ordena as arestas de acordo com os pesos
    
    for krus in range(len(Vertices)):
        if Vertices[krus][1] not in AGM or Vertices[krus][2] not in AGM:
            AGM.append(Vertices[krus][1]) #Coloca o vertice na lista de AGM (Vertice que representa a linha)
            AGM.append(Vertices[krus][2]) #Coloca o segundo na lista de AGM (Vertice que representa a coluna)
            lista = [] #Lista que vai receber os vertices
            lista.append(Vertices[krus][1])
            lista.append(Vertices[krus][2])
            lista.sort() #Ordenar os vertices
            Tabas.append(lista)
    Tabas.sort() #Ordena a lista dos ramos que vao ser construidos
    return Tabas
def Matriz(linha,coluna,valor):
    lista = []
    for l in range(linha):
        linha = []
        for c in range(coluna):
            linha.append(valor)
        lista.append(linha)
    return lista

cont = 0
while True:
    entrada = input().split()
    if int(entrada[0]) == 0:
        break
    else:
        cont+=1
        Grafo = Matriz(int(entrada[0]),int(entrada[0]),0)
        for i in range(int(entrada[1])):
            info = input().split()
            Grafo[int(info[0])-1][int(info[1])-1] = int(info[2])
        resultado = (Kruskal(Grafo))
        if cont > 1:
            print(' ')
        print('Teste %d' % (cont))
        for i in range(len(resultado)):
            print(str(resultado[i][0]) + ' ' + str(resultado[i][1]))
#FIM REDE OTICA
