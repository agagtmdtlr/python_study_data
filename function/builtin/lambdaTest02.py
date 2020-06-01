mylist = list(range(1,101))

lambda3bae = lambda x : x%3 == 0
newlist = list(filter(lambda3bae,mylist))
print(newlist)

lambda1 = lambda x : 3*x+2
newlist = list(map(lambda1,mylist))
print(newlist)


