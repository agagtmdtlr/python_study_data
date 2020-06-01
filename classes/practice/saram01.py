class human:
    nationality = '대한민국'
    def __init__(self,name,height,weight,hooby,blood):
        self.name = name
        self.height = height
        self.weight = weight
        self.hobby = hooby
        self.blood = blood

    def showInfo(self):
        msg = f'국적 : {self.nationality}\n' \
              f'이름 : {self.name}\n' \
              f'키 : {str(self.height)}\n' \
              f'몸무게 : {str(self.weight)}\n' \
              f'취미 : {self.hobby}\n' \
              f'혈액형 : {self.blood}'
        print(msg)