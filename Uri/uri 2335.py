ent = [int(x) for x in input().split()]
ent.sort()
menorS = ent[0] + ent[1]

if menorS == ent[2] or ent[0] == ent[1] or ent[1] == ent[2]:
    print("S")
else:
    print("N")
