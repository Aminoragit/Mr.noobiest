a = '하이'
b = '하이'
print(a==b) #int str 한글도 된다.


a = 0b00000101 #0101 = 5
print(a)

b = 0b00001101 #1101 = 13
print(b)

c = a&b
print(a,b,c)

#0b0000000 #binary 지원 해주는 편집기도 있고 없기도함(없으면 16진수로 표현 0x00)
c = a|b
print(a,b,c)

#파이썬에서는 비트연산 거의 안쓴다 하지만 논리연산은 많이 쓴다.

