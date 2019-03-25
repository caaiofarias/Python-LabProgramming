class Node:
    """ Classe que define um nodo simples de uma Estrutura de dados: (info, NextNodo)"""

    def __init__(self, data):
        """Construtor do Nodo"""
        self.data = data
        self.nextNode = None
    
    def getData(self):
        return self.data
    
    def setData(self,data):
        "Atribui valor ao Dado do nodo"
        self.data=data
    
    def getNextNode(self):
        "Retorna a referencia do proximo nodo"
        return self.nextNode
        
    def setNextNode(self,newNode):
        "Ajusta a referencia do proximo nodo"
        self.nextNode = newNode;  
class List:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
    
    def __str__(self):
        if self.isEmpty():
            return "A lista esta vazia!"
        correntNode = self.firstNode
        string = ""
        while correntNode is not None:
            string += str(correntNode.getData() )
            correntNode = correntNode.getNextNode()
        return string
        
    def insertAtBegin(self, value):
        newNode = Node (value) # instancia de um novo nodo
        if self.isEmpty(): #Insersao para Lista vazia
            self.firstNode = self.lastNode = newNode
        else:                   #Insersao para lista nao vazia
            newNode.setNextNode(self.firstNode)
            self.firstNode = newNode
    
    
    def insertAtEnd(self, value):
        newNode = Node(value)  #instancia de um novo nodo
        
        if self.isEmpty():  #Se a lista esta vazia
            self.firstNode = self.lastNode = newNode
        else:
            self.lastNode.setNextNode(newNode)
            self.lastNode=newNode
            
    def removeFromBegin(self):
        if self.isEmpty():
            return None
        firstNodeValue = self.firstNode.getData()
        if self.firstNode is self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            self.firstNode = self.firstNode.getNextNode()
        return firstNodeValue
        
    def removeFromEnd(self):
        if self.isEmpty():
            return None
        lastNodeValue = self.lastNode.getData()
        if self.firstNode is self.lastNode:
            self.firstNode=self.lastNode=None
        else:
            currentNode = self.firstNode
            while currentNode.getNextNode() is not self.lastNode:
                currentNode = currentNode.getNextNode()
            currentNode.setNextNode(None)
            self.lastNode = currentNode
        return lastNodeValue
    def isEmpty(self):
        return self.firstNode == None

    def getFirstNode(self):
        return self.firstNode
class Stack(List):

    def push(self,data):
        self.insertAtBegin(data)
    def pop(self):
        self.removeFromBegin()
class Queue(List):
    def push(self,data):
        self.insertAtEnd(data)
    def pop(self):
        return self.removeFromBegin()


festas = int(input())
casos = []
vencedor = 0
for festa in range(festas): # cada festa
    deck = Queue() # cria uma nova instancia da fila
    x = input().replace(" ","")
    for num in x:
        deck.push(int(num))
    x = input().replace(" ","")
    while x!='-1': 
        temp = Queue()
        for i in x:
            try:
                temp.push(int(i))
            except:
                continue
        casos.append(temp)
        x = input().replace(" ","")
    for i in range(1000):
        pivo = deck.pop()
        deck.push(pivo)
        for p in casos:
            if p.isEmpty() == True:#se a lista estiver vazia achei o vencedor
                vencedor = casos.index(p) + 1
                
            elif pivo == p.getFirstNode().getData():#primeiro verifico antes de tirar ou nao,:
                p.pop()                           #pois se a lista estiver vazia ele nao retorna  
            else:
                valor = p.getFirstNode().getData()#pego o primeiro elemento,
                p.push(valor)#insiro primeiro no fim
                p.removeFromBegin()#depois tira o elemento
            
        if vencedor > 0:
            break # sair do laço for p in casos
    if vencedor > 0:#sair do laço while caso seja >0 entao foi alguem
        print(vencedor)
        vencedor = 0
        casos = []
    else:           #senao, o vencedor foi Juvenal
        print(vencedor)
        vencedor = 0
        casos = []
