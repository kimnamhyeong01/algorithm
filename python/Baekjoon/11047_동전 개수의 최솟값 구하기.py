import time 
start_time = time.time()

n, k = input().split() 
n = int(n)
k = int(k)
a = [] 
sum = 0 
count = 0

for i in range(n):
    temp = int(input())
    a.append(temp)  

for j in a[::-1]:
    if j <= k:
        div = int(k / j) 
        count += div
        k = k - div * j
    if k == 0:
        break

print(count) 

end_time = time.time() 
print("시간:", end_time - start_time)