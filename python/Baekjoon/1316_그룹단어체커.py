n = int(input())
arr = []
cnt = 0
for _ in range(n):
    a = input()
    arr.append(a)

for i in range(n):
    temp = []
    temp = list(arr[i])
    checker = []
    for j in range(len(temp)):
        if temp[j] not in checker:
            checker.append(temp[j])
            continue
        elif temp[j] in checker: 
            if temp[j] == checker[len(checker) - 1]:
                checker.append(temp[j])
                continue
            else:
                break 
    if len(checker) == len(temp):
        cnt += 1
print(cnt)
