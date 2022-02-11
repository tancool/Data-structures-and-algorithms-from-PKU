def sequentialSearch(list,item):
    
    list_index = 0
    found = False

    while list_index<len(list) and not found:
        if list[list_index] == item:
            found = not found
        else:
            list_index = list_index + 1
    
    return found


def orderSearch(list,item):
    
    list_index = 0
    found = False
    while  list_index <len(list) and not found:
        if list[list_index] == item:
            found = not found
        else:
            if list[list_index] > item:
                found = not found
            else:
                list_index  = list_index + 1
    return found

test_list = [0,1,2,8,13,17,19,32,42]

print(sequentialSearch(test_list,42))
print(orderSearch(test_list,42))