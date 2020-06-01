if __name__ == '__main__':
    import saram01 as h
else:
    from . import saram01 as h
kim = h.human('김철수',172.5,72.5,'당구','AB')
kim.showInfo()