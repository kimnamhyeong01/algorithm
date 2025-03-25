def generate_binary(n: int) -> None: 
    for i in range(1, n+1):
        print(bin(i)[2:])# 이진수는 0b가 붙으므로 슬라이싱으로 제거 

#테스트 코드 
generate_binary(5)