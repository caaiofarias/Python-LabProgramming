class Node:
    """ Classe que define um nodo simples de uma Estrutura de dados: (info, NextNodo)"""

    def __init__(self, data):
        """Construtor do Nodo"""
        self.data = data
        self.nextNode = None
        self.antNode = None
    
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

    def setAntNode(self,newNode):
        self.antNode = newNode
        
    def getAntNode(self):
        return self.antNode

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

    def SearchNode(self,value):
        currentNode = self.firstNode
        while currentNode is not None:
            if currentNode.getData() == value:
                return currentNode
            else:
                currentNode = currentNode.getNextNode()
        if currentNode == None:
            return None

    def RemoveAtMiddle(self,value):
        currentNode = self.firstNode
        nodeRemover = self.SearchNode(value)
        if nodeRemover != None:
            if nodeRemover == self.firstNode:
                self.removeFromBegin()
            elif nodeRemover == self.lastNode:
                self.removeFromEnd()
            else:
                while currentNode.getNextNode() != nodeRemover:
                  currentNode = currentNode.getNextNode()
                currentNode.setNextNode(nodeRemover.getNextNode())
                nodeRemover.setNextNode(None)
                
        
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


class LDE():#Lista Duplamente Encadeada
    def __init__(self):
        self.firstNode = None
        self.LastNode = None

    def isEmpty(self):
        return self.firstNode == None

    def InsertAtBegin(self,value):
        newNode = Node(value)
        if self.isEmpty():
            self.firstNode = self.lastNode = newNode
        else:
            self.firstNode.setAntNode(newNode)
            newNode.setNextNode(self.firstNode)
            self.firstNode = newNode
    
    def RemoveAtBegin(self):
        if self.isEmpty():
            return None
        firstNodeValue = self.firstNode.getData()
        if self.firstNode == self.lastNode:
            self.firstNode = self.lastNode = None
        else:
            self.firstNode = self.firstNode.getNextNode()
            self.firstNode.setAntNode(None)
        return firstNodeValue

    def InsertAtEnd(self,value):
        newNode = Node(value)
        if self.isEmpty():
            self.firstNode = self.lastNode = newNode
        else:
            newNode.setNextNode(None)
            newNode.setAntNode(self.lastNode)
            self.lastNode.setNextNode(newNode)
            self.lastNode = newNode

    def RemoveAtEnd(self):
        lastNodeValue = self.lastNode.getData()
        if self.isEmpty():
            return None
        if self.lastNode is self.firstNode:
            self.lastNode = self.firstNode = None
        else:
            self.lastNode = self.lastNode.antNode
            self.lastNode.setNextNode(None)

    def Search(self,value):
        currentNode = self.firstNode
        while currentNode is not None:
            if currentNode.getData() == value:
                return currentNode
            else:
                currentNode = currentNode.getNextNode()
        if currentNode == None:
            return None
    def getFirstNode(self):
        return self.firstNode
        
    def RemoveAtMiddle(self,value):
        nodeRemover = self.Search(value)

        if nodeRemover != None:
            if nodeRemover == self.firstNode:
                self.RemoveAtBegin()
            elif nodeRemover == self.lastNode:
                self.RemoveAtEnd()
            else:
                nodeRemover.antNode.setNextNode(nodeRemover.nextNode)
                nodeRemover.nextNode.setAntNode(nodeRemover.antNode)
                nodeRemover.setNextNode(None)
                nodeRemover.setAntNode(None)
