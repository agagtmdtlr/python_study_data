mylist01 = [ 1,2,3,5 ]
mylist01 = [ idx for idx in range(1,5)]
print(mylist01)
mylist02 = [ 2,4,6,8 ]
mylist02 = [ 2*idx for idx in range(1,5)]
print(mylist02)
mylist03 = [idx for idx in range(1,101,3)]
print(mylist03,sum(mylist03))

#if
mylist04 = [ idx for idx in range(1,101,3) if idx%10 == 0]
print(mylist04)

for i in range(1,6):
    for j in range(1,6):
        print(j,end='')
    print()

for i in range(1,6):
    for j in range(1,6):
        print(i, end='')
    print()

for i in range(1,6):
    for j in range(i,i+5):
        print(j,end='')
    print()

for i in range(1,6):
    for j in range(10-i,5-i,-1):
        print(j,end='')
    print()

mytuple01 = tuple(idx for idx in range(1,6))
myset01 = {idx for idx in range(1,6)}

print(type(mytuple01),mytuple01)
print(type(myset01),myset01)

total = 0
for i in range(1,3):
    for k in range(5,8):
        total += i + k
print(total)
total = 0
for i in range(1,4,2):
    for k in range(2,6,3):
        total += 2 * i + k
print(total)