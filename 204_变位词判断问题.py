'''

只要有嵌套就要相乘起来

'''

'''
值得注意的是:
    - 计数器的比较法是拿空间换取时间.
'''

'''
# 解法3:暴力法
- 根据组合数学的结论，如果n个字符进行全排列其所有可能的字符串个数为
'''


def ContrastStrThree(s1,s2): # 解法4 => 计数比较 : 拿取空间换取时间. 时间复杂度为2n+ 26 == n
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos]+1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos]+1

    return_result = True
    j = 0
    
    while j< len(c1) and return_result:
        if c1[j] == c2[j]:
            j=j+1
        else:
            return_result = False
    
    return return_result
        


print(ContrastStrThree('aasds','sdsaa'))


