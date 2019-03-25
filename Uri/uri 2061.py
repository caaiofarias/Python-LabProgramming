ent = [int(x) for x in input().split()]
lista = []
for i in range(ent[1]):
    lista.append(input())

for i in lista:
    if i == "fechou":
        ent[0] -=1
        ent[0]+=2
    else:
        ent[0]-=1
print(ent[0])
