saved_pw = 'python'
count=3
while True : 
	input_str = input("password 입력 (나가시겠습니까? :quit) ==> ")

	if input_str == saved_pw:
		print('pw가 확인되었습니다')

	elif input_str == 'quit':
		break

	elif count==0 : 
		print('pw를 다시확인해 주시기 바랍니다.')
		break

	else:
		print('pw 실패')
		count+= -1
