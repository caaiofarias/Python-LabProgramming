def conta(string,achar):
    cont = 0
    i = 0
    f = len(achar)
    while f!=len(string)+1:
        if string[i:f] == achar:
            cont+=1
            i +=1
            f += 1
        else:
            i+=1
            f +=1
    return cont
        
resp = []
casos = 0
while True:
    try:
        ent1 = input()
        ent2 = input()
        qtd = conta(ent2,ent1)
        aux = 0
        casos += 1
        if qtd!= 0:
            ini = 0
            fim1 = len(ent1) 
            fim2 = len(ent2) 
            while ini < fim2:
                if ent1 == ent2[ini:fim1] and aux != qtd:
                    aux += 1
                    pos = ini
                    ini +=1
                    fim1 +=1
                else:
                    ini += 1
                    fim1 += 1
            print("Caso #%d:\nQtd.Subsequencias: %d\nPos: %d\n"%(casos,qtd,pos+1))
        else:
            print("Caso #%d:\nNao existe subsequencia\n"%(casos))
                
    except:
        break
