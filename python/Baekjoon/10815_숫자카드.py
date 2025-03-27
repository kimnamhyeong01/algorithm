from collections import deque
N = int(input()) 
answer = deque([])
s1 = set(map(int, input().split())) 
M = int(input()) 
s2 = list(map(int, input().split())) #list와 set의 차이: list는 입력 순서를 보장해주지만, set은 입력 순서를 보장해주지 않음. 그래서 s2를 set으로 바꿔서 실행시키면 원하는 결과를 얻을 수 없어서 s2는 list로 구현.

for i in s2:
    if i in s1:
        print(1, end = " ") 
    else:
        print(0, end = " ")


"""
----기존 이중 for문으로 구현한 부분 > 답은 맞으나 테스트 케이스 크기가 늘어나면 시간 초과----
for i in range(len(s2)):
    answer.append(0)
    for j in range(len(s1)):
        if s2[i] == s1[j]:
           answer.pop()
           answer.append(1)
           s1.remove(s1[j]) 
           break 
        else:
            pass 
print(*answer)
"""
 

 
# 사이트에 제시된 테스트 케이스는 정답 맞췄음. 근데 이중 for문을 써서, 백준 사이트 테스트에서 시간 초과 뜨는 듯함. 이중 for문을 제거한 코드를 생각해 봐야 할 듯.  
# >> 원래 s1, s2를 list로 정의하고 이중 for문을 썼다가, list 대신 속도가 더 빠른 deque로 바꿔봤는데도 시간 초과 뜸. 그냥 이중 for문을 쓰면 안될듯함.(답은 맞음) 
# 아직 C++에 익숙해져있나보다. 파이썬에서는 저런식으로 이중 for문으로 굳이 구현 안해도 if ~ in 이런식으로 구현해도 알아서 탐색해주는데. 더 공부해야 할 부분인듯하다.
# 근데 이 문제는 어차피 if ~ in 으로 해도 시간 초과 발생. 그럴만도 한 게 M이 500,000 까지니까..list에서 비교하는 방식으로 전부 다 비교하면 무조건 시간초과. 
# 그래서 이럴 때 list, deque 보다도 해쉬 방식으로 구현된 dict나 set을 사용하면 시간 초과 해결! >> 값이 일치하는 지 비교할 때는 역시 
# 해쉬가 무조건 빠르다는 걸 체감할 수 있었던 문제. 
# 해쉬 함수와 dict, set에 대한 공부가 더 필요할 듯. 