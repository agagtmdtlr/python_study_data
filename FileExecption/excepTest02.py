
def checkjum(mylist):
    try:
        avg = sum(mylist)/len(mylist)
        if avg >= 60:
            print('합격')
        else:
            msg = '{} : 불합격'.format(avg)
            raise Exception(msg)
    except Exception as err:
        print(err)
mylist = [70,60,30]
# 평균 점수가 60미만이면 예외를 발생시키는 프로그램 작성
checkjum(mylist)