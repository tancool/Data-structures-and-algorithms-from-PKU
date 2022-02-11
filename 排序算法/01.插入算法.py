# 插入算法
def insertion_sort(arr):
    for i in range(1,len(arr)): # 默认将第一个元素设置为已排序.
        current = arr[i] # 当前需要主动与遍历元素要进行对比的值
        pre_index = i-1 # 往前一步
        while pre_index >=0 and arr[pre_index] > current: # 限制条件:下标>=0 且前一个元素大于当前元素
            arr[pre_index+1] = arr[pre_index] # 将元素往后面赋值一位.
            pre_index -= 1
        arr[pre_index+1] = current # 跳出循环条件.插入元素
    return arr

# print(insertion_sort([11,33, 36, 39, 44, 55, 66, 69, 77, 88, 99,11, 22, 33, ]))
print(insertion_sort([3,44,2,5,47,15]))