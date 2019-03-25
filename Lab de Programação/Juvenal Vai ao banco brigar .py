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

casos = int(input())

listaFila = []
final = []
for i in range(casos):
    regular = Queue()
    pref = Queue()
    passos = int(input())
    for op in range(passos):
        x = input()
        if x.isdigit():
            break
        if len(x) > 1:
            temp = x.split()
            if temp[0] == "f":
                regular.push(temp[1])
            else:
                pref.push(temp[1])
        elif len(x) == 1:
            if x == "A":
                if regular.isEmpty() == True:
                    pref.pop()
                else:
                    regular.pop()
            elif x == "B":
                if pref.isEmpty() == True:
                    regular.pop()
                else:
                    pref.pop()
            else:
                if regular.isEmpty() == True:
                    listaFila.append(0)
                else:
                    listaFila.append(int(regular.getFirstNode().getData()))
                if pref.isEmpty() == True:
                    listaFila.append(0)
                else:
                    listaFila.append(int(pref.getFirstNode().getData()))
    final.append(listaFila)
    listaFila = []
c = 0
for i in final:
    print("Caso %s:"%(final.index(i)+1))
    for j in range(len(i)):
        print(i[j],end=" ")
        c+=1
        if c == 2:
            c = 0
            print("")
            continue
