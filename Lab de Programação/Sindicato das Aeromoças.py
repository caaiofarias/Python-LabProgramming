from collections import defaultdict
import heapq

# min heap
class MinHeap:

	def __init__(self):
		self._queue = []
		self._index = 0

	def insert(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def remove(self):
		return heapq.heappop(self._queue)[-1]

	def get_length(self):
		return len(self._queue)

# grafo
class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		self.vertexes = {}

	def addEdge(self, src, dest, cost):
		self.graph[src].append((dest, cost))
		self.vertexes[src] = src
		self.vertexes[dest] = dest

	def dijkstra(self, src, dest):

		# obtém o número de vértices
		number_vertexes = len(self.vertexes)

		# estimativas de menor custo
		p = [None for i in range(number_vertexes)]

		# estima para origem é 0
		p[src] = 0

		# constrói a min heap
		min_heap = MinHeap()

		# insere a origem na min heap
		min_heap.insert(src, 0)

		# enquanto o tamanho da fila for maior que 0
		while min_heap.get_length() > 0:

			# remove da fila de prioridades
			u = min_heap.remove()

			# percorre os adjacentes de "u"
			for edge in self.graph[u]:

				# obtém o vértice adjacente e o custo
				v, cost = edge

				# relaxamento
				if p[v] is None or p[v] > p[u] + cost:

					# atualiza a estimativa de custo
					p[v] = p[u] + cost

					# insere na fila de prioridades
					min_heap.insert(v, p[v])

		# retorna o custo do menor caminho
		return p[dest]

g = Graph()#Constroi o Grafo
entrada = input().split()
for i in range(int(entrada[1])):
        casos = [int(x) for x in input().split()]
        g.addEdge(casos[0],casos[1],casos[2]) #Add as arestas no g

resp = []
for i in range(2,len(g.graph)):#Tirando o caminho da origem
        resp.append(g.dijkstra(0,i))# Roda o dijkstra e imprime o menor deles
print(min(resp))
