N, K = map(int, input().split()) 
A = [0] * N
for i in range(N):
    A[i] = int(input()) 

count = 0

for j in range(N - 1, -1, -1):
    if A[j] <= K:
        count += int(K/A[j])
        K = K % A[j]

print(count)