entrada = [int(x) for x in input().split()]
cont = 0
listaPlanos = []
listaPlanetas = []
for i in range(entrada[0]):
    p = input()
    listaPlanos.append(p.split())
for j in range(entrada[1]):
    p = input()
    listaPlanetas.append(p.split())
dir = 0
esq = 0
maior = 0
cent = 0
A,B,C,D,x,y,z = 0,0,0,0,0,0,0

for plano in range(len(listaPlanos)):
    A = int(listaPlanos[plano][0])
    B = int(listaPlanos[plano][1])
    C = int(listaPlanos[plano][2])
    D = int(listaPlanos[plano][3])
    for planeta in range(len(listaPlanetas)):
        x = int(listaPlanetas[planeta][0])
        y = int(listaPlanetas[planeta][1])
        z = int(listaPlanetas[planeta][2])
        if A*x + B*y + C*z  == D:
            cent += 1
        elif A*x + B*y + C*z == 0:
            continue
        else:
            if A*x + B*y + C*z - D<0:
                esq += 1
            else:
                dir += 1
    if dir > esq and dir > cent:
        maior = dir
        esq = 0
        dir = 0
        cent = 0
    elif esq > dir and esq > cent:
        maior = esq
        esq = 0
        dir = 0
        cent = 0
    elif cent > dir and cent > esq:
        maior = cent
        esq = 0
        dir = 0
        cent = 0
print(maior)
        
