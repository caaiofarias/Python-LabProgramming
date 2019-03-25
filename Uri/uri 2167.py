ent = int(input())
ent2 = [int(x) for x in input().split()]
maior = ent2[0]
cont = 0
r = False
for i in range(1,ent):
    if ent2[i] >= maior:
        maior = ent2[i]
    else:
        maior = ent2[i]
        print(i+1)
        r = True
        break
        
if r == False:
    print(0)
