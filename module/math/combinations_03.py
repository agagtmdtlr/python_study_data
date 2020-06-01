import math as m
import copy
from itertools import *

def combinations1(lists,r):
    n = len(lists)
    par = m.factorial(n)
    chi = m.factorial(r)*m.factorial(n-r)
    return par/chi


def defined(x1):
    x2 = copy.deepcopy(x1)
    x2[0] =2

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

man = ['이순신', '김유신', '강감찬', '안중근', '김홍도', '권율']
woman = ['유관순', '조마리아', '신사임당', '황진이']

# mr = combinations1(man,3)
# wr = combinations1(woman,2)
#
# result = mr*wr
# print(result)

result1 = list(combinations(man,3))
result2 = list(combinations(woman,2))
r1 = []
r2 = []
for i in result1:
    r1.append(list(i))
for i in result2:
    r2.append(list(i))

ss = [(i,j) for i in r1 for j in r2]
for i in ss:
    print(i)
print(len(ss))