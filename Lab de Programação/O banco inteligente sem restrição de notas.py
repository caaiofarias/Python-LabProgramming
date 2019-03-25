saque = int(input())
quant = {}
temp = input().split()
quant[2],quant[5],quant[10],quant[20],quant[50],quant[100] = int(temp[0]),int(temp[1]),int(temp[2]),int(temp[3]),int(temp[4]),int(temp[5])
def retornaPossib(saque,nota=[2,5,10,20,50,100]):
    global quant
    comb = [0]*(saque+1)
    comb[0] = 1
    for valor in nota:
        for i in range(1,len(comb)):
            if i >= valor:
                comb[i] += comb[i-valor] 
    return comb
x = retornaPossib(saque)

print(x[saque])

                
