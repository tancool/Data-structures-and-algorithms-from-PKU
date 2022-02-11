def add_num(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + add_num(numList[1:])
print(add_num([1,3,5,7,9]))

# a = [1,2,3,4,5]
# print(a[1:])