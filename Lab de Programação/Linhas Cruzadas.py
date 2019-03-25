vert = int(input())
hori = [int(x) for x in input().split()]
resp = 0
for i in range(1,vert+1):
    temp = i
    while hori[temp-1] > i or hori[temp-1] != i:
        if hori[temp-1] > i:
            resp += 1
        temp+=1
        if temp >= vert:
            break
    else:
        continue
print(resp)
