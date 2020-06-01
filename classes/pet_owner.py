# from pyy.classes import mypet as pe
# import mypet as pe # 아니 이게 왜됨????
if __name__ == "__main__" or __name__ == "decimal":
 	import mypet as pe
else:
 	from . import mypet as pe
print(__name__)
dog01 = pe.Pet('삽살이',3,'사료')
dog01.eat()
dog01.sleep()
print('-'*30)

cat01 = pe.Pet('야옹이', 4)
dog01.eat()
dog01.sleep()
print('-'*30)