mystr = 'Aa1'
#Return True if the string is a digit string,
# False otherwise.
#A string is a digit string
# if all characters in the string are digits
# and there is at least one character in the string.
print(mystr[0].isdigit())
print(mystr[2].isdigit())

#a(97), A(65), 0(48)
#ord() 함수는 문자를 ascii 코드로 바꿔주는 함수 입니다.
print(ord(mystr[1]))