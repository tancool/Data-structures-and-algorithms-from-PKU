
def merge_sort(arr):
    
    if len(arr) == 1:# 首先是递归.需要找出终止条件
        return arr

    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]
    return merge(merge_sort(left),merge_sort(right))

def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:

        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    result += left
    result += right
    return result




print(merge_sort([79,84,21,6]))
print(merge_sort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]))