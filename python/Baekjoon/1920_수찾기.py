key = 0
N = int(input())
test1 = set(map(int, input().split()))
M = int(input())
test2 = list(map(int, input().split()))


for num in test2:
    if num in test1:
        print(1)
    else:
        print(0)