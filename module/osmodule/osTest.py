import os

print(os.name)

print('현재 폴더 하위에 새 폴더 생성하기')
save_path = input('생성할 폴더 이름 : ')

# print(os.path.isdir('sample'))
# print(os.path.exists('sample'))
# print(os.path.getsize('sample'))
# os.path.join('sample','os')
# if not os.path.isdir('os'):
#     os.mkdir('os')

if not os.path.isdir(save_path):
    # mkdir : Make DIRectory
    os.mkdir(save_path) # page 251
else :
    print('이미 존재하는폴더 입니다.')
    # 하위 폴더에 폴더 folder01~folder10까지 만들어 보기
    for i in range(1,11):
        foldername = 'folder'+str(i).zfill(2)
        # print(foldername)
        newfolder = os.path.join(save_path,foldername)
        os.mkdir(newfolder)

print('finished')
