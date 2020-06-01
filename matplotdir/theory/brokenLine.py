import numpy as np
import matplotlib.pyplot as plt

x1 = [idx for idx in range(1,8)]
y1 = [30,70,60,40,30,55,60]

x2 = [idx for idx in range(1,8)]
y2 = [40,60,80,50,50,70,80]

# ymax : y축 최대 눈금
ymax = max(max(y1),max(y2)) + 1
ymin = min(min(y1),min(y2))

# 글씨 ( 인코딩 )
plt.rc('font',family='Malgun Gothic')

# 그래프 그리기
plt.plot(x1,y1)
plt.plot(x2,y2)

# 단위 표시 (눈금 표시)
plt.xticks(np.arange(0,7+1), ('','국어','영어','수학','과학','도덕','국사','생물'))
plt.yticks(np.arange(ymin,ymax,5))

# 축이름
plt.xlabel('과목')
plt.ylabel('점수')

# 표 이름
plt.title('학생별\n시험 점수')
# 라벨 이름
plt.legend(labels=['김철수','홍길동'])

plt.grid(True)

plt.show()
