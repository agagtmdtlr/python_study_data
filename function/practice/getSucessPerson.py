# 다음과 같이 출력해주는 함수를 작성해 보세요.
# 점수가 60이상이면 합격입니다.
def findGrade(scores):
    result = []
    for i in scores :
        if i >= 60 :
            grade = '합격'
        else:
            grade = '불합격'
        result.append((grade,i))
    return result


scores = [80, 50, 90, 60]
result = findGrade(scores)
print(result)