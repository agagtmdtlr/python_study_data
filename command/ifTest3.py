# 월 입력 : 2
# 2월은 겨울 입니다.
month = int(input('월 입력 : '))
season = None


if month <= 11 and month >= 9:season='가을'
elif month <= 8 and month >= 6:season='여름'
elif month <= 5 and month >= 3:season='봄'
else:season='겨울'
print(season)