entrada=[int(x) for x in input().split()]
planos = []
planetas = []
nPlanetas= [0]*entrada[0]
for i in range(entrada[0]):
    plano = [int(x) for x in input().split()]
    planos.append(plano)
for j in range(entrada[1]):
    planeta = [int(x) for x in input().split()]
    planetas.append(planeta)

A = 0
B = 0
C = 0
D = 0
X = 0
Y = 0
Z = 0

for i in range(len(planos)):
    A = int(planos[i][0])
    B = int(planos[i][1])
    C = int(planos[i][2])
    D = int(planos[i][3])
    for p in range(len(planetas)):
        X = int(planetas[p][0])
        Y = int(planetas[p][1])
        Z = int(planetas[p][2])
        if A != 0 and X != 0:
            if A*X + B*Y + C*Z <= D:
                nPlanetas[i] += 1
        elif B!=0 and Y!= 0:
            if A*X + B*Y + C*Z <= D:
                nPlanetas[i] += 1
        elif C!= 0 and Z!= 0:
            if A*X + B*Y + C*Z <= D:
                nPlanetas[i] += 1
        elif A*X + B*Y + C*Z > D:
            continue
print(max(nPlanetas))
