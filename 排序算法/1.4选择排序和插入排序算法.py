
# 选择排序
def selection_sort(arr):
    for i in range(len(arr)-1):  # 控制的是比较次数.(最后一个是最大的,默认不用比较)
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[min_index],arr[i] = arr[i],arr[min_index]
    return arr

#print(selection_sort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]))
#返回结果 [11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]

# 插入算法
def insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        pre_index = i-1

        while pre_index >=0 and arr[pre_index] > current:
            arr[pre_index+1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index+1] = current
    return arr

# insertion_sort([11,33, 36, 39, 44, 55, 66, 69, 77, 88, 99,11, 22, 33, ])
print(insertion_sort([33,22,11]))


# 返回结果[11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]
# a = [1,2,3,4]
# a [0] = a[1]
# print(a)