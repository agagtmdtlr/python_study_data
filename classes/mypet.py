class Pet:
    def __init__(self,name,no,food='생선'):
        self.name = name
        self.no = no
        self.food = food

    def eat(self):
        msg = '%s가 %s를 먹습니다.' %(self.name,self.food)
        print(msg)

    def sleep(self):
        msg = '%s가 %s시간 잠을 잡니다.' %(self.name,str(self.no))
        print(msg)
print(__name__)