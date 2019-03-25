casos = int(input())

for i in range(casos):
    bonus = int(input())
    dab = [int(x) for x in input().split()]
    gua = [int(x) for x in input().split()]
    if dab[2] %2 == 0 and gua[2] %2 !=0:
        atkD = (dab[0] + dab[1])/2 + bonus
        atkG = (gua[0] + gua[1])/2
        if atkD > atkG:
            print("Dabriel")
        elif atkD == atkG:
            print("empate")
        else:
            print("Guarte")
    elif gua[2] %2 == 0 and dab[2]%2!= 0:
        atkG = (gua[0] + gua[1])/2 + bonus
        atkD = (dab[0] + dab[1])/2
        if atkG > atkD:
            print("Guarte")
        elif atkD == atkG:
            print("empate")
        else:
            print("Dabriel")
        
    elif gua[2] %2 != 0 and dab[2]%1 != 0:
        atkG = (gua[0] + gua[1])/2
        atkD = (dab[0] + dab[1])/2
        if atkG > atkD:
            print("Guarte")
        elif atkD == atkG:
            print("empate")
        else:
            print("Dabriel")
    else:
        atkD = (dab[0] + dab[1])/2 + bonus
        atkG = (gua[0] + gua[1])/2 + bonus
        if atkG > atkD:
            print("Guarte")
        elif atkD == atkG:
            print("empate")
        else:
            print("Dabriel")
        
        
        
