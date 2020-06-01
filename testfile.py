def sum_digit(num):
    num = str(num)
    sum = 0
    for i in range(len(num)):
        sum = sum + int(num[i])
    return sum

print(sum_digit(123))