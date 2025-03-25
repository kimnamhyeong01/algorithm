from collections import deque 

def josephus(N, k):
    people = deque(range(1, N+1)) 
    result = []  

    while people:
        for _ in range(k - 1):
            people.append(people.popleft())
    
    return result 

N, k = 7, 3 
print(josephus(N, k))