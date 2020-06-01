import math as m

def combinations(lists,r):
    n = len(lists)
    par = m.factorial(n)
    chi = m.factorial(r)*m.factorial(n-r)
    return par/chi

man = ['이순신','김유신','강감찬']
result = combinations(man,2)
print(result)