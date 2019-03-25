res = 0
def resolve(s,minv):
    global res
    global memory
    if minv == 6:
        if s == 0:
            return 1
        else:
            return 0
    if memory[s][minv]>=0:
        return memory[s][minv]
    q = s//notas[minv]
    if q > n[minv]:
        q = n[minv]
    for i in range(q):
        news = s - i * notas[minv]
        res+= resolve(news,minv+1)
    memory[s][minv] = res
    return res
memory = []
saque = int(input())
notas = [2,5,10,20,50,100]
n = [int(x) for x in input().split()]
for v in range(saque+1):
    linha = []
    for i in range(6):
        linha.append(-1)
    memory.append(linha)
        
        
x = resolve(saque,0)
