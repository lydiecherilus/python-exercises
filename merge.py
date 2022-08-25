'''Write a Python script to merge two Python dictionaries'''

def merge(dic1, dic2):
    j = dict()
    for i in (dic1, dic2):
        j.update(i)
    print(j)

merge({1:10, 2:20}, {3:30, 4:40})
