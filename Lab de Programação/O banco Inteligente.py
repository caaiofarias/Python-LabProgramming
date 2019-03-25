saque = int(input())
quant = [int(x) for x in input().split()]
notas = [2,5,10,20,50,100]
comb = [0]*(saque+1)
comb[0] = 1
for i in range(len(quant)-1,-1,-1):
    for j in range(saque,-1,-1):
        for k in range(1,quant[i]+1):
            if j-k*notas[i]>=0 and k<=quant[i]:
                comb[j]+=comb[j-k*notas[i]]#somo a quantidade de notas * a nota sem o valor do saque que é da anterior
print(comb[saque])
