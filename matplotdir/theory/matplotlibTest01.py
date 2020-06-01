import matplotlib.pyplot as plt

# matplotlib 한글 지원 안됨. 글꼴을 변경하면 됨
plt.rc('font',family='Malgun Gothic') # default 설정하기
plt.plot([1,2,3,4], 'gD:')
plt.xlabel('x축 한글 표시')
plt.title('그래프 Test')
plt.show()
print('finished')