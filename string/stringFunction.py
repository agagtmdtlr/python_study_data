mystring = 'Hello python!'

# print('길이 :', len(mystring)) # 길이 구해버리기
# print('알파벳 \'o\'포함 개수 :', mystring.count('o')) #부분 카운팅하기
# print('검색 위치1 :', mystring.find('e')) #(찾을값,탐색 시작 위치,탐색 끝 위치)
#
# print('검색 위치2 :', mystring.find('o',6))
# print('검색 위치4 :', mystring.rfind('o')) #함수 이름의 접두사에 r이 붙으면 right의 줄인말입니다.
#
# print('검색 위치3 :', str.find(mystring,'o',6))
# print('검색 위치4 :', mystring.find('o',6,7)) #찾으면 해당 위치 값 / 못찾으면 -1값 반환

# print('문자열 치환1 :', mystring.replace('l','t'))
# print('문자열 치환2 :', mystring.replace('l','t',1))
# print('문자열 치환3 :', mystring.replace('l','blue'))

# mystring = '  가나   다라  '
# print('공백 지우기1 : [',mystring.strip(),']', sep='')
# print('공백 지우기2 : [',mystring.lstrip(),']', sep='')
# print('공백 지우기3 : [',mystring.rstrip(),']', sep='')
# mystring = 'www.example.com'
# print('공백 지우기4 : [',mystring.strip('cmow.'),']', sep='')
# print('대문자 :', mystring.upper())
# print('소문자 :', mystring.lower())

# print('문자열 분할 : ',mystring.split('.'))
# print('문자열 분할 : ',mystring.split('.',1))
# print('문자열 분할 : ',mystring.rsplit('.',1))

mystring = 'hello_python.xls'
# print('시작 여부 : ',mystring.startswith('H'))
# print('시작 여부 : ',mystring.endswith('.ppt'))
print('첫 글자만 대문자 : ',mystring.capitalize())
mylist = ['삼성','엘지','대우']
#문자1.join(반복객체) : '문자2'를 연결할 때,
# 구분자로 '문자1'을 사용하세요
print('join 함수 : ',' and '.join(mylist))

