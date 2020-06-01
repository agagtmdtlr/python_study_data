import numpy as np

def checks(lists):
    return all([elem for elem in lists])

lists = []
print(bool(lists))
lists = [[],[],[],[1]]
print(checks(lists))