n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
arr = []
T = list(t)
cnt = 0 
for i in range(n):
    cnt = 0
    temp = ''
    temp = str[i]
    for j in range(len(T)):
        if temp[j] == T[j]:
            cnt += 1
        else: 
            continue 
    if cnt == len(T):
        arr.append(temp) 
arr.sort()
print(arr[k - 1])        
     