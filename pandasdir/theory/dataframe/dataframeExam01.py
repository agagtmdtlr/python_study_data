from pandas import DataFrame

sdata = {
    '도시':['서울','서울','서울','부산','부산'],
    'year':['2000','2001','2002','2001','2002'],
    'pop':[1.5,1.7,3.6,2.4,2.9]} # key : column index

myindex = ['one','two','three','four','five'] # row index

myframe = DataFrame(data=sdata , index=myindex)
# print(myframe)
# print(type(myframe))
# print('-'*20)
#
# myframe.index.name = '호호호'
# print(myframe.index) # 행 색인 : Index # object : 문자
# print('-'*20)
#
# myframe.columns.name = '하하하'
# print(myframe.columns) # 열 색인 : Index # object : 문자
# print('-'*20)
# print(myframe)

print(myframe.values,type(myframe.values))
print('-'*20)
print(myframe.dtypes)

print(myframe.T)

mycolumns = ['pop','year','도시'] # 칼럼 색인 이름 짓기
newframe = DataFrame(sdata,columns=mycolumns,index=myindex)
print(newframe)