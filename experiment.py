import os
import os.path as p


def count_symbols(st, symbol='\\'):
    count = 0
    for i in st:
        if i == symbol:
            count += 1
    return count


tree = []
countTabs = 1
for folder, folders, files in os.walk('C:/Users/Terc1a/Desktop/ziq/'):
    path = p.abspath(folder)
    countTabs = count_symbols(path)
    tabs = "   " * (countTabs - 1)
    out = tabs + str(p.basename(folder))
    print(out)
    for file in files:
        tabs = "   " * countTabs

        out = tabs + str(p.basename(file))
        print(out)
