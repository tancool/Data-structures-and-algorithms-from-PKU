def selection_sort(input_arr):
    
    for i in range(len(input_arr)-1):# 默认最后一个是最小的
        min_index = i

        for j in range(i+1,len(input_arr)):

            if input_arr[j] < input_arr[min_index]:
                min_index = j

        if(min_index != i):
            input_arr[min_index],input_arr[i] = input_arr[i],input_arr[min_index]
    
    return input_arr


print(selection_sort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]))