

'''
- 变位词
    - 长度相等,但是位置不同

- python不支持字符串的修改
'''

'''
为了简单起见，假设参与判断的两个词仅由小写字母构成，而且长度相等
'''

def ContrastStr(s1,s2): # 解法1: 逐字检查

    alist = list(s2)
    pos_1 = 0
    contrastStr_result = True

    while pos_1< len(s1) and contrastStr_result:
        
        pos_2 = 0
        is_found = False

        while pos_2<len(alist) and not is_found: # 到这里是对比完毕
            if s1[pos_1] == alist[pos_2]:
                is_found = True
            else:
                pos_2 = pos_2+1
        
        if is_found:
            alist[pos_2] = None
        else:
            contrastStr_result = False
        
        pos_1 = pos_1+1
    
    return contrastStr_result


# print(ContrastStr('hlel','hell'))

'''
可知其数量级为O(n^2)
'''


def ContrastStrTwo(s1,s2): # 解法2: 排序 => 算法复杂度是 O(n)
    
    list_s1 = list(s1)
    list_s2 = list(s2)
    list_s1.sort()
    list_s2.sort()
    pos =0
    return_result = True

    while pos<len(list_s1) and return_result:
        if list_s1[pos] == list_s2[pos]:
            pos = pos+1
        else:
            return_result = false
    
    return return_result

    #return list(s1) == list(s2) # 可以直接这么写


print(ContrastStrTwo('he3ll','h3lle'))


