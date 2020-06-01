kim = ['김철수',10,20]
lee = ['이순신',30,40]
park = ['박영희',50,60]

name = [kim[0],lee[0],park[0]]
total = [sum(kim[1:]),sum(lee[1:]),sum(park[1:])]
print(name,total,sep='\n')
mylist = [ [i[0],sum(i[1:])] for i in [kim,lee,park]]
name = [ i[0] for i in [kim,lee,park]]
total = [ sum(i[1:]) for i in [kim,lee,park]]
print(mylist,name,total,sep='\n')