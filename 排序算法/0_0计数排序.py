def CountingSort(arr):
    max_num = max(arr) # 最大值
    min_num = min(arr) # 最小值
    length = max_num - min_num + 1 # 数组出现次数
    tempArr = [0 for i in range(length)]
    retArr = [0 for i in range(length-1)]

    # 第一次循环 => 判断出现的次数
    for num in arr:
        # 7 - 4 = 3 
        tempArr[num-min_num] +=1

    # 第二次循环 => 判断之前的出现过多少次
    for i in range(1,length):
        tempArr[i] = tempArr[i-1] + tempArr[i]

    # 第三次循环 => 进行输出

    for j in range(len(arr)-1,-1,-1):
        num_in_tempArr = arr[j] - min_num # j在tempArr中的位置
        subtractCount = tempArr[num_in_tempArr] - 1 #tempArr[num_in_tempArr]是前面有多少个比他大的.-1就是这个数字本身的下标位置
        tempArr[num_in_tempArr] -=1 # 减去次数
        retArr[subtractCount] = arr[j]

    return retArr

if __name__=='__main__':
    # arr=[12,25,26,13,14,25,12,17,18,14]
    arr = [7,5,4,9,4]
    print(CountingSort(arr))
