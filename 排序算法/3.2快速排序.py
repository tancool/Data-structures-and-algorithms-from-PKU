'''
侧重分解,简化合并
'''

def quick_sort(arr):
    """快速排序"""
    if len(arr) < 2:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = arr[len(arr) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)

    for item in arr:
        # 大于基准值放右边
        if item >= mid:
             right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)


# arr = [11, 99, 33, 69, 77,5, 88, 55, 11, 33, 36, 39, 66, 44, 22]
arr = [6,15,8,7]
print(quick_sort(arr))
 
#返回：[11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]



def quick_sort_for_book(array, l, r):
    if l < r: # 递归继续条件
        q = partition(array, l, r) # q是中间的锚点
        quick_sort_for_book(array, l, q - 1) # left
        # print('<<')
        quick_sort_for_book(array, q + 1, r) # right

def partition(array, l, r):
    x = array[r] # 数组最后一个元素作为对比.
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
            print(array)
    array[i + 1], array[r] = array[r], array[i+1]

    return i + 1

arr1 = [8,6,15,14,13]
quick_sort_for_book(arr1,0,len(arr1)-1)
print(arr1)