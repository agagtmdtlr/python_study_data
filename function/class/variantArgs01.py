def func(*args):
    total = 0
    for item in args:
        total += item
    print('총합 :',total)

func(1,2)
func(5,6,7)