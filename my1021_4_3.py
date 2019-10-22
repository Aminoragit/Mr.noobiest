def functest(): #함수정의 : 함수가 동작할 내용을 정의
	print("hello python")
	print('python function')
	print('test')
	d=256
	print('id() : ',id(d)) #d는 c와 같은 1000값이지만 d가 func의 값이므로 다른 id를 가지게 된다. #단 ver2와 같이 256이면 같은 id를 가진다.
	

c=256
print('id(c) : ',id(c))

print('main start!!')
print('='*50)

functest()  #함수 호출 : 함수 정의 부분으로 점프
print('='*50)

print('main stop!!')


