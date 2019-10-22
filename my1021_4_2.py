a = 200
b = 200
c = 200

print(id(a))
print(id(b))
print(id(c)) #-5~256은 파이썬에서 미리 id를 만들어놓은 정수 객체이다. 따라서 a,b,c의 id는 모두 같다. 벗어난 값은 따로 생성

d= 278
print(id(d)) #계속 바뀐다

c=1000
d=1000
print(id(c))
print(id(d)) #어? 1000인데 id가 같네? -> 파이썬 ver때문에 그럼(ver2는 256까지인데, 얜 ver3라 됨)

