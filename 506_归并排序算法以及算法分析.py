
def mergeSort(alist):

    if len(alist) > 1: # 递归运行条件
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)


        i = 0; j = 0; k = 0 # i => left下标,j => right下标,k => alist下标

        while i < len(lefthalf) and j < len(righthalf): # 如果left和 right均不为空

            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

alist = [21,152,33,3241,54,654,423,12,32]
alist = [4,3,2,1,99]
mergeSort(alist)
print(alist)


def marge_sort(lst):

    if len(lst) <= 1: # 递归结束条件
        return lst

    middle = len(lst) // 2 # 分解

    left = marge_sort(lst[:middle])
    right = marge_sort(lst[middle:])


    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    merged.extend(right if right else left)
    return merged

alist_ = [21,152,33,3241,54,654,423,12,32]
alist_ = [4,3,2,1,99]
print(marge_sort(alist_))