string = 'hello'
mylist = list({ord(i) for i in string})
mylist.sort()
print(mylist)
print([chr(i) for i in mylist])