n = int(input())
k = int(input())
p=0
vet = [int(x) for x in input().split()]

def ok(x):
    qtd = 0
    for i in range(k):
        qtd+=vet[i]//x
        if qtd>=n:
            return True
    
    return False
def buscab(m):
    i =  1
    f = m
    ans = 0
    while i <= f:
        q = (i+f)//2
        if(ok(q)):
            ans = max(q,ans)
            i= q+1
        else:
            f = q-1

    return ans


for i in range(k):
    p = max(p,vet[i])

print(buscab(p))
    
