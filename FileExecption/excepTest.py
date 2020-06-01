

try:
    mydict = {'hong':10,'kim':20}
    print(mydict['choi'])

    su1 = 10
    su2 = '20'

    result = su1 + su2
    print(result)
except TypeError as err:
    print(err)
except KeyError as err:
    print(err)
except Exception as err:
    print(err)
else:
    print('no err')
finally:
    print('program end')