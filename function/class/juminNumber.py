def findSsn(no):
    result = '잘못된'
    # 문자를 숫자로 변환 후 비교 주의
    if len(no)==14:
        if no[6]=='-' :
            if (no[0:6]+no[7:]).isdigit() :
                if int(no[7]) in range(1,5) :
                    if int(no[2]) in range(0,2):
                        result = '올바른'
                    else:
                        result = '월 범위 초과 오류'
                else:
                    result = '성별 digit 번호 오류'
            else:
                result = '숫자형식 외 문자 오류'
        else:
            result = '- 미기입 오류'
    else:
        result = '총 14자리 오류'
    return result

# 총 14자리어야 합니다.
# 6번째 요소는 '-'이어야 하고, 나머지는 모두 숫자이어야 합니다.
# 2번째 : 0또는 1이어야 합니다.
# 7번째 : 1, 2, 3, 4 중의 하나이어야 합니다.
exam1 = ['701226-1710566',
         '7012261710566',
         '703426-1710566',
         '701226-5710566']
for x in exam1:
    print(f'주민번호 {x}는 {findSsn(x)} 형식 입니다')
# print(exam1[0][0:6]+exam1[0][7:])
# print(type(exam1[0][0:6]))
# 7012261710566
# <classes 'str'>