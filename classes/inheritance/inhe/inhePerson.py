class Person: # 이름, 나이, 성별
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def aboutMe(self): # 변수 정보를 출력
        print(f'이름 : {self.name}\n'
              f'나이 : {str(self.age)}\n'
              f'성별 : {self.gender}')

class Employee(Person): # 급여 , 입사일
    def __init__(self, name, age, gender, salary, hiredate):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hiredate = hiredate


    def Work(self): # 일하기 동작
        print(f'{self.name}님 열심히 일합시다.')

    def aboutMe(self): # 오버라이딩
        super().aboutMe() # 은닉화 방지
        print(f'급여 : {str(self.salary)}\n'
              f'입사 일자 : {self.hiredate}')

class Student(Person): # 과목 , 학점
    def __init__(self,name,age,gender,subject,grade):
        super(__class__,self).__init__(name,age,gender)
        self.subject = subject
        self.grade = grade
    def doStudy(self): # 공부하기
        print(f'{self.name}님 열심히 공부합시다.')

    def aboutMe(self): # 오버라이딩
        super().aboutMe()
        print(f'과목 : {self.subject}\n'
              f'성적 : {self.grade}')

class Teacher(Person):
    def __init__(self,name,age,gender,subject):
        super().__init__(name,age,gender)
        self.subject = subject

    def teach(self):
        print(f'{self.name}님 열심히 가르칩시다.')

    def aboutMe(self): # 오버라이딩
        super().aboutMe()
        print(f'과목 : {self.subject}')
#이름, 나이, 성별, 급여 , 입사일, 과목 , 학점
#일반화 보편적인 변수 수퍼, 특화된 변수 서브

soo = Employee('김철수',20,'남자',50000,'2018/12/25')
soo.aboutMe()
soo.Work()

hee = Student('박영희',19,'여자','국어','A학점')
hee.aboutMe()
hee.doStudy()

kim = Teacher('김유신',40,'남자','파이썬')
kim.aboutMe()
kim.teach()