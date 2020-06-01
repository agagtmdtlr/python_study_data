import random

def jusawee(su):
    total = 0
    for idx in range(su):
        rnd = random.randint(1,6)
        total += rnd
        print(f'{idx+1}번째 값 : {rnd}')
    print(f'총합 : {total:2d}')
sido = 10
jusawee(sido)
