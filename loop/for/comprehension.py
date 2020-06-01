name = ['hong','kim','lee']
age = [20,40,50]
human = {name:age for name,age in zip(name,age)}
print(human)

name = [['hong',20],['kim',40],['lee',50]]
human = {i[0]:i[1] for i in name}
print(human)

gntor = (i for i in range(1,11,2))
