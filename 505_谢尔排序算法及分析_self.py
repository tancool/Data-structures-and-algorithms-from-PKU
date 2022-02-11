def shellSort(alist):
    list_count = len(alist) // 2 # 分为多少份.每次除以2.最低是1(while做限制).

    while list_count > 0: # 做限制

        for start_position in range(list_count): # 分块
            getInsertionSort(alist,start_position,list_count) # 使用插入排序函数
        
        list_count = list_count // 2 



def getInsertionSort(alist,start,gap): # 插入排序抽象

    for i in range(start+gap,len(alist),gap): # start+gap 是起始对比下标

        current_value = alist[i]
        now_index = i

        while now_index>=gap and alist[now_index-gap] > current_value: 
            # now_index>=gap是做一个限制.

            alist[now_index] = alist[now_index-gap]
            now_index = now_index - gap
        
        alist[now_index] = current_value

alist = [21,152,33,3241,54,654,423,12,32]
shellSort(alist)
print(alist)

