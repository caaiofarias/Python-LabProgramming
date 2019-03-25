class No:

    def __init__(self, dado):
        self.dado = dado
        self.filesquerdo = None
        self.fildireito = None
        self.pai = None
    
    def getDado(self):
        return self.dado
    
    def setDado(self,novo):
        self.dado = novo
    
    def getFilhoLeft(self):
        return self.filesquerdo
    
    def setFilhoLeft(self,esquerdo):
        self.filesquerdo = esquerdo
        
    def getFilhoRight(self):
        return self.fildireito
    
    def setFilhoRight(self,direito):
        self.fildireito = direito
    
    def getPai(self):
        return self.pai
    
    def setPai(self,pai):
        self.pai = pai
    
class ArvoreBinaria:
    
    def __init__(self):
        self.raiz = None
    
    def getRaiz(self):
        return self.raiz
    
    def setRaiz(self, novaR):
        self.raiz = novaR
        
    def Buscar(self,x):
        i = self.raiz
        while i is not None and x != i.getDado():
            if i.getDado() != x:
                if x < i.getDado():
                    i = i.getFilhoLeft()
                else:
                    i = i.getFilhoRight()
            else:
                break
        return i
    
    def Minimo(self,x):
        while x.getFilhoLeft() != None:
            x = x.getFilhoLeft()
        return x
    
    def Maximo(self,x):
        while x.getFilhoRight() != None:
            x = x.getFilhoRight()
        return x
    
    def Sucessor(self,x):
        x = self.Buscar(x)
        if x.getFilhoRight() != None:
            return self.Minimo(x.getFilhoRight())
        else:
            y = x.getPai()
            while y != None and x == y.getFilhoRight():
                x = y
                y = x.getPai()
        return y.getDado()
    
    
    def Predecessor(self,x):
        x = self.Buscar(x)
        if x == None:
            return '0'
        if x.getFilhoLeft() != None:
            f=self.Maximo(x.getFilhoLeft())
            return str(f.getDado())
        y = x.getPai()
        if y == None:
            return '0'
        elif x == y.getFilhoRight():
            return str(y.getDado())
        else:
            while x == y.getFilhoLeft():
                x = y
                y = x.getPai()
                if y == None:
                    return '0'
        return str(y.getDado())
    
    def Inserir(self,z):
        z = No(z)
        y = None
        x = self.getRaiz()
        while x != None:
            y = x
            if z.getDado() < x.getDado():
                x = x.getFilhoLeft()
            else:
                x = x.getFilhoRight()
        z.setPai(y)        
        if y == None:
            self.setRaiz(z)
        else:
            if z.getDado() < y.getDado():
                y.setFilhoLeft(z)
            else:
                y.setFilhoRight(z)
    
    def Deletar(self,z):
        x = self.Buscar(z)
        if x is None:
            return False
        else:
            if x.getFilhoLeft() == None or x.getFilhoRight() == None:
                y = x
            else:
                y = self.Sucessor(x.getDado())
            if y.getFilhoLeft() != None:
                h = y.getFilhoLeft()           
            else:
                h= y.getFilhoRight()
            if h!= None:
                h.setPai(y.getPai())
            if y.getPai() == None:
                self.setRaiz(h)
            else:
                if y == y.getPai().getFilhoLeft():
                    y.getPai().setFilhoLeft(h)
                else:
                    y.getPai().setFilhoRight(h)
            if y != x:
                x.setDado(y.getDado())    
        return y
    
    def Ordem(self, x,resin):
        if x != None:
            self.Ordem(x.getFilhoLeft(),resin)
            resin.append(str(x.getDado()))
            self.Ordem(x.getFilhoRight(),resin)
    
    def PreOrdem(self, x, respre):
        if x != None:
            respre.append(str(x.getDado()))
            self.PreOrdem(x.getFilhoLeft(),respre)
            self.PreOrdem(x.getFilhoRight(),respre)
        
    def PosOrdem(self, x, respos):
        if x != None:
            self.PosOrdem(x.getFilhoLeft(),respos)
            self.PosOrdem(x.getFilhoRight(),respos)
            respos.append(str(x.getDado()))

ncasos = 1
while True:
    try:
        casos = int(input())
        arvore = ArvoreBinaria()
        print("Caso: %d"%(ncasos))
        ncasos += 1
        for i in range(casos):
            op = input().split(" ")
            if op[0] == "A":
                arvore.Inserir(int(op[1]))
            elif op[0] == "B":
                arvore.Deletar(int(op[1]))
            elif op[0] == "C":
                print(arvore.Predecessor(int(op[1])))
                
            elif op[0] == "PRE":
                listaPre = []
                z = ' '
                arvore.PreOrdem(arvore.getRaiz(),listaPre)
                if listaPre == []:
                    print(0)
                else:
                    for i in range(len(listaPre)):
                        z+= listaPre[i] + " "
                    print(z.strip())

            elif op[0] == "IN":
                listaIn = []
                x = ' '
                arvore.Ordem(arvore.getRaiz(),listaIn)
                if listaIn == []:
                    print(0)
                else:
                    for i in range(len(listaIn)):
                        x+= listaIn[i] + " "
                    print(x.strip())
                
            elif op[0] == "POST":
                listaPos = []
                y = ' '
                arvore.PosOrdem(arvore.getRaiz(),listaPos)
                if listaPos == []:
                    print(0)
                else:
                    for i in range(len(listaPos)):
                        y+= listaPos[i] + " "
                    print(y.strip())
    except:
        break
