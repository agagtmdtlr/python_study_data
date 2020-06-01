mydict = {'박정희':10 , '이명박':20, '김대중':30, '노무현':40}

# 키로 정렬시 김/노/박/이
result = sorted(mydict.keys())
print(result)

result = sorted(mydict.keys(),reverse=True)
print(result)
# 값으로 정렬시 박/이/김/노
result = sorted(mydict.values())
print(result)

print('# 값으로 역순 정렬하되 key를 보여주기')
result = sorted(mydict.keys(),key=mydict.get,reverse=True)
print(result)