k = int(input()) 
stack = [] 
answer = 0
for k in range(0, k):
    i = int(input()) 
    if i == 0 and len(stack) != 0: 
        stack.pop() 
    else:
        stack.append(i)   

for j in range(0, len(stack)):
    answer += stack.pop() 

print(answer) 
