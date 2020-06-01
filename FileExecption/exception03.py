def gfriendCheck(finddata):
    gfriend = ['은하','소원','유주','예린','신비','엄지']
    isMember = False # 가정 : 멤버가 아니라고 가정합니다.

    #반복문
    if finddata in gfriend :
        isMember = True

    if isMember == True:
        print('여자 친구 멤버가 맞아요')
    else:
        msg = finddata + '여자 친구 멤버가 아닙니다'
        raise Exception(msg)

name= '신비'
try:
    gfriendCheck(name)
except Exception as err:
    print('예외 발생 : {}'.format(err))