str1 = 'Hello Korea'

print(str1[0])
print(str1[1],str1[6])
print(str1[-3])


#'KHa'가 출력되게 인덱싱해보세요
print(str1[6],str1[0],str1[-1],sep='')

print(str1[0:5]); print(str1[:5])

#[begin:end:step]
print(str1[0:7:2])

# 주민 번호 앞자리와 뒤자리를 출력하세요
# 이분의 성별은?
ssn = '881120-1234567'
form =f"""앞자리 : {ssn[:6]}
뒤자리 : {ssn[7:]}
성별 : """
if int(ssn[7]) == 1 or int(ssn[7]) == 3 :
    form += "남"
else :
    form += "여"
print(form)

today = '20200225rainy'
i = today
year = i[:4]
month = i[4:6]
day = i[6:8]
weather = i[8:]
form = f"""{year}년 {month}월 {day}일
날씨 : {weather}"""

print(form)