a, b = map(int, input().split()) 
c = list(map(int, input().split()))  
res = [0] 
temp = 0
for i in c:
    temp = temp + i 
    res.append(temp) 
print(res)
for i in range(b):
    n1, n2 = map(int, input().split())
    print(res[n2] - res[n1 - 1]) 
