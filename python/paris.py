T = int(input())
N, M = map(int, input().split())
arr = []
total = 0
max_kill = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
    temp = [] 

for i in range(N - M + 1):
    for j in range(N - M + 1):
        
        total = 0
        for x in range(M):
            for y in range(M):
                total += arr[i + x][j + y] 

        max_kill = max(max_kill, total)
print(f"#{t} {max_kill}")
