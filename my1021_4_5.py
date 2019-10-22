str1='python is'
str2='  good programming'
str3 = str1 + str2

#string 연산자 overloding 원래+는 사칙연산이라 숫자만 되는데 파이썬에서 내부에서.__add__가 써지는것임
str1.__add__(' ') #str 덧셈=__add__ 메서드
print(str3)

print('='*40) #=


print('len :', len(str1)) #문자열의 길이 length = len

mylist = [3,6,.8, 0]
print('list len : ' , len(mylist))

print(str1[0],str1[1],str1[-1]) ## -1대신 str1[len(str1)-1] 써도 됩니다.

print(str1[:-1]) #분할연산(:)
print(str1[1:4:1]) #확장 분할 연산(start:end:jump)

print(str1[::-1]) #거꾸로
