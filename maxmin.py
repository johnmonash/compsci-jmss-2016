
def max (datalist):
    biggest = datalist[0]
    for item in datalist:
        if biggest < item:
            biggest = item
    return biggest

def min (datalist):
    smallest = datalist[0]
    for item in datalist:
         if smallest > item:
             smallest = item
    return smallest