def plus5(su):
    return su + 5

su1 = 14
result = plus5(su1)
print(f'결과 : {result}')
print(f'결과2 : {plus5(100)}')

for idx in range(3,12,4):
    print(idx,':',plus5(idx))