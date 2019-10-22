from decimal import Decimal

string_object = "python programming"

total=[] # 빈 리스트 생성
print(total,type(total))

for ch in string_object: #ch안에 string_object를 리스트 화하는것.
	if ch == " ":
		total.append(ch)
	else:
		total.append(chr(ord(ch)-32))   #append는 list에 내용 추가해주는 함수  #ord는 아스키 코드로 변호한 chr은 다시 문자열로 변환 -32한것은 대문자로 표현
print(ord('p')) #ord는 아스키 코드로 바꿔주는건데 구글로 검색하면 편하다.
print(chr(68)) #chr은 아스키 코드를 문자로 표현해준다. --D 
               #Q1 그럼 16진수를 사용하는 명령어는 없나요?
print(total,type(total))

#########################################################################################################################

string_big = "".join(total) #join은 ''없이 합쳐라 라는 명령어다.
							#Q2 그럼 string_big은 리스트가 아닌 통짜 str인가요? = yes 타입으로 확인할수 있어요
print(string_big,type(string_big))

print('='*50)

#######################맨위의 아스키를 사용해 대문자로 표현하는것을 간결하게 표현하는 방법####################################

string_big_upper = string_object.upper() #소문자를 대문자로 변환해주는 함수
print(string_big_upper)

#########################################################################################################################

x=Decimal('0.1') + Decimal('0.2')
print(x)
