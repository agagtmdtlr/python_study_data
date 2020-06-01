# 후보 인원 수: 2
# 투표 내용 : 1 1 2 2 2
# [2, 3]
# 기호 : 1, 득표 수 :2
# 기호 : 2, 득표 수 :3
# 최다 득표자: 기호2

# countingVotes : 각 후보들의 득표 수를 list로 반환해 줍니다.
def countingVotes(numbers, votes):
    earns = dict()
    for i in votes:
        if i in earns :
            earns[i] = earns[i] + 1
        else:
            earns[i] = 1
    print(earns)
    list1 = sorted(earns.keys())
    list2 = [earns[i] for i in list1]
    print(list1,list2,sep='\n')
    return list2


# printMaximum : 최다 득표자의 정보를 출력해 줍니다.
def printMaximum(earns):
    maxre = getMaxInfo(earns)
    print(f'최다 득표자 : 기호 {maxre}번')


# getMaxInfo : 최다 득표자의 기호 번호를 반환 해주는 함수입니다.
def getMaxInfo(earns):
    result = 0
    for i in range(1,len(earns)):
        if earns[result] < earns[i]:
            result = i
    return result+1


number = 2
votes = [1,1,3,2,2,2,3,4,5,5,2]
earns = countingVotes(number,votes)
print(earns)
for i in range(len(earns)):
    print(f'기호 {i+1}번 : {earns[i]}표')
printMaximum(earns)