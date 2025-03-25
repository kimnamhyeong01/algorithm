def solution(n: int): 
    q: list[int] = [1] 
    answer: int = 1
    i: int = 1 
    total: int = 1
    mid: int = (n + 1) // 2
    while i < mid:
        i += 1 
        total += i 
        q.append(i) 
        while total > n: 
            total -= q.pop(0)
        if total == n:
            answer += 1 
    return answer 
#테스트 코드 
print(solution(15)) 
print(solution(20)) 

