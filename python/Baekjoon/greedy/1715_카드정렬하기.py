from queue import PriorityQueue

pq = PriorityQueue()

N = int(input())

for _ in range(N):
    temp1 = int(input())
    pq.put(temp1)

sum = 0
var1 = 0
var2 = 0
temp2 = 0

while pq.qsize() > 1:
    var1 = pq.get()
    var2 = pq.get() 
    temp = var1 + var2
    sum += temp 
    pq.put(temp)

print(sum)
        