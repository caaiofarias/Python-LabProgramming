entrada = int(input())
tabela = {}
resp = 0
for i in range(entrada):
    shoe = input().split()
    if shoe[0] not in tabela:
        tabela[shoe[0]] = [0,0]
        if shoe[1] == "E":
            tabela[shoe[0]][1] +=1
        else:
            tabela[shoe[0]][0] += 1
    else:
        if shoe[1] == "E":
            tabela[shoe[0]][1] +=1
        else:
            tabela[shoe[0]][0] += 1

for i in tabela:
    D= tabela[i][0]
    E = tabela[i][1]
    if D == 0 or E == 0:
        continue
    elif D == E:
        resp += (D+E)//2
    else:
        if D >= E:
            resp += (sum(tabela[i]) - (D-E)) // 2
        elif E >=D:
            resp += (sum(tabela[i]) - (E-D)) // 2
print(resp)
