class Information:
    def __init__(self,name):
        self.name = name
        print(self.name + ' 생성자가 호출되었습니다.')
        self.result = 0

    def __del__(self):
        print(self.name+' 소멸자')
        print('주로 마감 작업용으로 사용됩니다.')

    def add(self,num):
        self.result += num
        print(f'{num}로 더합니다.')
        return self.result

    def sub(self,num):
        self.result -= num
        print(f'{num}로 뺍니다.')
        return self.result

    def mul(self,num):
        self.result *= num
        print(f'{num}로 곱합니다.')
        return self.result

    def div(self,num):
        if num is 0:
            num = 5
            self.result /=num
        else:
            self.result /=num
        print(f'{num}로 나눕니다.')
        return self.result


kim = Information('김유신')
print(kim.add(10))
print(kim.sub(5))
print(kim.mul(10))
print(kim.div(5))
