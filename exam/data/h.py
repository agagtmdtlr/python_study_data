import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

mycolors = ['blue', 'green', 'red', 'c']

data = ['강호동', '유재석', '이수근', '전현무', '강호동', '유재석', '이수근', '강호동', '유재석', '강호동']

mydict = {}  # 빈도 수를 저장할 사전

for d in data:
    if d in mydict:
        mydict[d] += 1
    else :
        mydict[d] = 1

slices = []
mylabels = []
for key, value in mydict.items():
    slices.append(value)
    mylabels.append(key)

plt.pie(x=slices,startangle=90,autopct='%.2f%%',labels=mylabels,explode=[0,0.1,0,0],counterclock=False,shadow=True)


plt.legend(loc='best')

filename = 'pieGraph02.png'
plt.savefig(filename, dpi=400, bbox_inched='tight')
print(filename + ' 파일이 저장되었습니다.')
plt.show()