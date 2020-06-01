import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')

hobbies = ['잠자기','외식','영화 감상','운동']
slices = [10,20,30,40]
# RRGGBB 색 조합표
mycolor = ['blue','#6AFF00','#FF00CC','yellow']

# startangle = 시작 각도 , counterclock = 반시계 방향
# exploce = (해당 slice를 밖으로 도출시킨다.) , shadow = 그림자
plt.pie(slices,labels=hobbies,autopct='%.2f%%',colors=mycolor,
        startangle=90,counterclock=False, explode=(0.3,0.2,0.1,0),
        shadow=True)
plt.legend(loc='best')

filename = 'data/myhobbies.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+'파일 저장 완료')

plt.show()