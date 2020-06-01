import re

#패턴.split(문자열) : 문자열 분리하기
print('\n# split 함수')
fruits = '사과 오렌지#배,감'
regex = '[ #,]'
pattern = re.compile(regex)
result = pattern.split(fruits)
print(type(result))
print(result)

#패턴.sub('new문자열',문자열) : 문자열 치환하기 substitude(in<->out)
print('\n# sub 함수')
mystr= '광복절 1945-08-15'
regex = '-'
pattern = re.compile(regex)
result = pattern.sub('/',mystr)
print(type(result)) #반환 타입 : str
print(result)


#패턴.subn('new문자열',문자열, count=정수) : 문자열 전체에서 count 만큼 치환하기
print('\n# subn 함수')
mystr = '01-02-03-04-05'
regex = '-'
pattern = re.compile(regex)
for idx in range(1,5):
    result = pattern.subn('/',mystr,count=idx)
    print(result) #type tuple