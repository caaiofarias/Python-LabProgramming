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
vencedor = 0 
casos = []
festas = int(input())
for i in range(festas):
    deck = Queue()
    x = input().split()
    for num in range(len(x)):
        deck.push(int(x[num]))
    while x[0] != '-1':
        temp = Queue()
        x = input().split()
        if x[0] == "-1":
            break
        else:
            for num in range(len(x)):
                temp.push(int(x[num]))
            casos.append(temp)
    for rodada in range(1000):
        pivo = deck.pop()
        deck.push(pivo)
        for p in casos:
            if p.isEmpty():
                vencedor = casos.index(p) + 1
            elif p.getFirstNode().getData() == pivo:
                p.pop()
            else:
                flag = p.pop()
                p.push(flag)
        if vencedor > 0:
            break
    if vencedor > 0:
        print(vencedor)
        vencedor = 0
        casos = []
    else:
        print(vencedor)
        casos = []
    
