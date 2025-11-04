N = int(input())
plusarray = []
minusarray = [] 
one = 0
zero = 0
temp1 = 0
sum = 0 

dump = 0

for _ in range(N):
    temp1 = int(input())
    if temp1 > 0 and temp1 != 1:
        plusarray.append(temp1)
    elif temp1 == 0:
        zero += 1
    elif temp1 == 1:
        one += 1
    else:
        minusarray.append(temp1)

plusarray.sort()
while len(plusarray) > 1:
    var1 = plusarray[len(plusarray) - 1] 
    var2 = plusarray[len(plusarray) - 2]
    sum = sum + var1 * var2 
    plusarray.pop()
    plusarray.pop() 

if len(plusarray) == 1:
    sum += plusarray[0] 

minusarray.sort(reverse = True)
while len(minusarray) > 1: 
    var1 = minusarray[len(minusarray) - 1]
    var2 = minusarray[len(minusarray) - 2]
    sum = sum + var1 * var2 
    minusarray.pop()
    minusarray.pop() 

if len(minusarray) == 1 and zero > 0:
    sum = sum + minusarray[0] * 0 
elif len(minusarray) ==1 and zero == 0:
    sum = sum + minusarray[0] 
else: 
    dump += 1

sum += one 
print(sum)