is_object='python' #class str의 객체
is_object.upper() #string class의 메소드 upper() 접근
print(is_object)
print(is_object.upper())


mydict = {'a':3, 'b':4,'c':5} 
print(mydict['b'])

mydict['d'] = 99 #추가할수도 있다.
print(mydict,type(mydict)) #사전처럼 단어와 뜻이 표현하는 것처럼 
			  			   #순서대로 표현된다고 해서 시퀸스 타입은 아니다. mapping타입이다.
for item in range(5):
	print(item,type(item),id(item))
print('='*50)
for item2 in mydict:
	print(item2,type(item2),id(item2))
	print('='*50)
	print(mydict[item2])

