'''
vetor = ["pares de pregos ligados por uma linha"]
indice do vetor representa os pregos na vertical, e o
inteiro em cada pos, os pregos na horizontal.

i(vertical) e j(horizontal) entao:
    vetor[i] = j

pregos a(vertical) e pregos b(horizontal)

se a>i and b<j or a<i and b>j

a e i(são indices) b e j(são os elemntos salvos na pos)
'''

def merge(p,n):
        global vet
        global aux
        if n <= 1:
                return 0
        c = merge(p,n//2) + merge(p+n//2,n-n//2)
        d,a,b = 0,0,n//2
        while d<n:
                if a != n//2 and (b == n or vet[p+a]<vet[p+b]):
                        aux[d] = vet[p+a]
                        a+=1
                else:
                        aux[d] = vet[p+b]
                        c+=n//2+a
                        b+=1
                d+=1
        for i in range(n):
                vet[p+i] = aux[i]
        return c

entrada = int(input())
vet = [int(x) for x in input().split()]
aux = [0]*entrada
print(merge(0,entrada))
