# 比对时间复杂度 O(n^2)
# 交换时间复杂度 O(n^2)

# 冒泡排序在链式存储也可以使用冒泡排序,适应性比较广.
# 中间监控




# 基于冒泡排序优化的选择排序

# 比对时间复杂度 O(n^2)
# 交换时间复杂度 O(n^2)

def bubbleSort(alist):

    for pass_num in range(len(alist)-1,0,-1): # 比对次数
        for i in range(pass_num):
            if alist[i+1] <  alist[i]:
                alist[i],alist[i+1] = alist[i+1] ,alist[i]
    return alist

print(bubbleSort([2661,312,321,321,54,654,423,12,32,312]))


def bubbleSort_II(alist): # 性能改进
    exchanges = True
    pass_num = len(alist) - 1
    while pass_num >0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if alist[i+1] <  alist[i]:
                exchanges = True
                alist[i],alist[i+1] = alist[i+1] ,alist[i]
        pass_num = pass_num -1
    return alist

print(bubbleSort([21,312,321,321,54,654,423,12,32,312]))