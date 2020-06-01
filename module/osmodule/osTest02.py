import os

# /로 표현하면 한번만, \로 표현하려면 두번 적어주세요
myfolder = 'c:\\windows'

print(os.listdir(myfolder))

filelists = os.listdir(myfolder)
for one in filelists:
    who = os.path.join(myfolder,one)
    if os.path.isfile(who) :
        # print('파일 :',one)
        # print(os.path.splitext(who),end=' , ')
        ext = os.path.splitext(who)[-1]
        if ext == '.exe':
            print('파일 :',one)
    # else :
        # print('폴더 :',one)