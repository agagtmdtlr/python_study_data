mystr = 'abcd'

str_len = 10 # 전체길이
fill_str = '=' # 채워넣을 문자

#ljust(전체길이, 채워넣을 문자) :오른쪽에 채워짐
result = mystr.ljust(str_len,fill_str)
print(result)

result = mystr.rjust(str_len,fill_str)
print(result)

#zfill(자리수) : 모자라는 곳은 0(zero)으로 채워라(fill)
result = mystr.zfill(str_len)
print(result)