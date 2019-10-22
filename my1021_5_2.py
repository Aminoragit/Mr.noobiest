mystr= "hello python programming"

count=0
for s in mystr :       	
 	if s == 'o':
 		count += 1
 	#print(s,' ', end='')
else:
	print()

print('o의 갯수는? : ',count) #위의 if문을 사용해서 갯수를 셀수있다.
print('pro' in mystr) #in은 안에 값이 있는지에 따라 true false가 결정된다.



