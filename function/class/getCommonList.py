def getCommonList(list_A,list_B):
    set_A = set(list_A)
    set_B = set(list_B)
    result = set_A.intersection(set_B)
    return result
list_A = ['이순신', '김유신', '강감찬', '이봉창',
          '안중근', '윤봉길']
list_B = ['김춘추', '이순신', '김유신', '최영']

result = getCommonList(list_A,list_B)
print(result)