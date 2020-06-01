name,age,height,blood = input('이름,나이,키,혈액형').split(',')
age = int(age)
height = float(height)
#출력 예시:
format1 = f"""이름(name) : {name}
나이(age) : {age}
키(height) : {height}
혈액형(blood) : {blood}
"""
print(format1)