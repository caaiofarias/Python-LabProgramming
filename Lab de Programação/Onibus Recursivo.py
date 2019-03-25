n,inicio,chegada = [int(x) for x in input().split()]
lista = [[] for x in range(n+1)]
for x in range(1,n):
    a,b = [int(x) for x in input().split()]
    lista[a].append(b)
    lista[b].append(a)

def procura(lista,atual,chegada,anterior,contador):
    if atual == chegada:
        print(contador)
        return None
    else:
        for j in lista[atual]:
            if j!= anterior:
                procura(lista,j,chegada,atual,contador+1)
procura(lista,inicio,chegada,None,0)
