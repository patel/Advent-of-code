

def get_index(col, row):
    return ((col + row - 1) * (col + row) / 2) - row + 1

def get_code(index):
    code = 20151125
    while index > 1:
        code = (code * 252533) % 33554393
        index = index - 1
    return code

print get_code(get_index(3075, 2981))

'''Output
9132360
'''