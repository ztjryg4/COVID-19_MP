import json


def select(order):
    '''
    0: brief
    1: tips
    2: detail
    3: info
    '''
    filename = [
        'data/brief.txt',
        'data/tips.json',
        'data/detail.json',
        'data/info.json'
    ]
    if order == 0:
        f = open(filename[order], "r")
        line = f.readline()
        return line
    else:
        f = open(filename[order], "r")
        line = f.readline()
        return line


def update(order, data):
    '''
    0: brief
    1: tips
    2: detail
    3: info
    '''
    filename = [
        'data/brief.txt',
        'data/tips.json',
        'data/detail.json',
        'data/info.json'
    ]
    if order == 0:
        f = open(filename[order], "w+")
        f.write(data)
        return data
    else:
        f = open(filename[order], "w+")
        js = json.dumps(data, ensure_ascii=False)
        f.write(js)
        return data
