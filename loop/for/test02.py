# 파일 이름 : maxScore.pyy

# 다음 3학생의 국영수 시험 점수입니다.
# 3학생 중에서 평균 점수가 가장 높은 학생의 정보를 출력하세요.
# 출력 결과
# 최고 평균은 park이고, 평균은 80.0입니다.
# 최저 평균은 kim이고, 평균은 66.7입니다.

kim  = [50, 80, 40]
park = [80, 90, 50]
lee  = [70, 50, 60]
dict1 = dict()
dict1['kim'] = sum(kim)/len(kim)
dict1['park'] = sum(park)/len(park)
dict1['lee'] = sum(park)/len(park)
maxv = list(['',0])
minv = list(['',100])

for idx,val in dict1.items() :
    if maxv[1] < val :
        maxv[0] = idx
        maxv[1] = val
    if minv[1] > val :
        minv[0] = idx
        minv[1] = val
print(f'최고 평균은 {maxv[0]}이고, 평균은 {maxv[1]:.2f}입니다.\n최고 평균은 {minv[0]}이고, 평균은 {minv[1]:.2f}입니다.')

# 최고 평균은 80.0입니다.
# 최저 평균은 66.7입니다.
list2 = [sum(kim)/len(kim),sum(park)/len(park),sum(park)/len(park)]
print(f'최고 평균 : {max(list2):.2f}, 최저 평균 : {min(list2):.2f}')
