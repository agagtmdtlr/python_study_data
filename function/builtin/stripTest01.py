print('strip()은 좌우 공백 제거')
string = '   가나다라    '
result = string.strip()
print('[%s]' %string)
print('[%s]' %result)

print('\nstring(\'a\')은 좌우측의 문자 a제거')
string = 'aa가나다라aa'
result = string.strip('a')
print('[%s]' %result)

print('\nrstrip()은 우측에만 관여합니다.')
print('lstript() 함수도 있습니다.')
string = 'aa가나다라aa'
result = string.rstrip('a')
print('[%s]' %result)
