class Calculator:
    def __init__(self,lists):
        self.lists = lists

    def sum(self):
        result = 0
        for no in self.lists:
            result += no
        print(f'합계 : {result}')

    def avg(self):
        lens = len(self.lists)
        result = sum(self.lists)/lens
        print(f'평균 : {result:.1f}')


cal1 = Calculator([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculator([6,7,8,9,10])
cal2.sum()
cal2.avg()