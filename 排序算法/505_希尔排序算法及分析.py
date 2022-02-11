def shellSort(alist):
    sublistcount = len(alist)//2 # 子列表个数.
    
    while sublistcount > 0:

        for startposition in  range(sublistcount):
            getInsertionSort(alist,startposition,sublistcount)
            
            
            print("After increments of size",sublistcount,'The list is ',alist)

        sublistcount = sublistcount // 2


def getInsertionSort(alist,start,gap): # 插入排序
    for i in range(start+gap,len(alist),gap): # 如果start+gap > len(alist). python会直接跳出循环
        current_value = alist[i]
        position = i
        while position>=gap and alist[position-gap] > current_value: 
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = current_value


alist = [21,152,33,3241,54,654,423,12,32]
shellSort(alist)
print(alist)