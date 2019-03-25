res = [0]
cont = 1
while True:
    try:
        lista2 = []
        ent = int(input())
        for i in range(ent+1):
                for j in range(i):
                    lista2.append(i)
                res = lista2
        if ent == 0:
            print("Caso %d: 1 numero"%(cont))
            print(0)
            print("\n")
            cont += 1
        else:
            print("Caso %d: %d numeros"%(cont,len(res)+1))
            cont += 1
            print(0,end = " ")
            for i in range(len(res)):
                print(res[i],end = " ")
            print("\n")
    except:
        break
