'''
- 二分查找时间复杂度 O(logn)

- 最好的排序时间复杂度是 O(logn)

- 在有序表的的查找和开销是O(n)级的

- 切片的时间复杂度是O(k)的.
    - 切片操作的复杂度是O(k)，这样会使整个算法的时间复杂度稍有增加

'''

def binary_search(sort_list,search_value):

    start_index = 0
    end_index = len(sort_list)-1
    count = 0
    result = False
    while start_index <= end_index:

        middle = (start_index + end_index) // 2
        count = count +1
        if sort_list[middle] == search_value:
           result= not result # 返回其所查找下标与查找次数
        elif sort_list[middle] < search_value: #  要查找的值大于中间值,在右边.
            start_index = middle + 1
        else:
            end_index = middle - 1
    return result
test_list = [0,1,2,8,13,17,19,32,42]

# print(binary_search([test_list],3))

print(binary_search([2,3],13))