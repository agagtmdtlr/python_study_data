import matplotlib.pyplot as plt

wordInfo = {'강감찬':40, '이순신':20, '윤봉길':30, '안중근':10}
plt.rc('font',family='Malgun Gothic')

abc = sorted(wordInfo, key=wordInfo.get, reverse=True)
print(abc) # for xticks

defg = sorted(wordInfo.keys(),reverse=True)
print(defg)

hijk = sorted(wordInfo.values(), reverse=True)
print(hijk) # for graph concat_data y asix

plt.xlabel('학생이름')
plt.ylabel('빈도수')

mycolor = ['r','g','b','m']

# plt.bar(x=range(len(wordInfo)),height=hijk,color=mycolor,align='center')
# plt.xticks(range(len(wordInfo)),abc,rotation=0)

plt.bar(x=abc,height=hijk,color=mycolor,align='center')

plt.show()