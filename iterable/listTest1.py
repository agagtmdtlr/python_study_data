mylist = ['강감찬','김유신']
print(mylist[0]) #인덱싱

#list.append() 맨뒤에다가 추가
mylist.append('이순신')
mylist.append('안중근')

print(mylist)

mylist.insert(2,'이성계')
#mylist = ['강감찬', '김유신', '이성계', '이순신', '안중근']
print(mylist[::2])
print(mylist[:len(mylist)])
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
# print(mylist.remove('김유신'))

mylist.reverse()
newlist = ['윤봉길','신사임당']
mylist.extend(newlist)
print(mylist)
mylist.append('강감찬')
print(mylist.count('강감찬'))
print(mylist.index('강감찬',1))

print(mylist.index('강감찬',mylist.index('강감찬')+1))

if mylist.count('강감찬') is 2 :
    print()