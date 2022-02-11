

def max_violent(arr):# 使用暴力破解法.
    max_value = -100
    index_for_left =0
    index_for_right =0
    for i in range(len(arr)):
        for j in range(i,len(arr)):

            temporary_value = 0
            
            for k in range(i,j+1):
                temporary_value = temporary_value + arr[k]
            
            if temporary_value>max_value:
                max_value = temporary_value
                index_for_left = i
                index_for_right = j
    
    return (max_value,index_for_left,index_for_right)



arr = [-2,2,-3,4,-1,2,1,-5,3] # 最大和是6
print(max_violent(arr))





# 最大连续子数组的和
l =  [-2,2,-3,4,-1,2,1,-5,3]

# 下面有一个错误,j需要减去1. print(l[3:7]) => 这有一个错误 l[3:7)

# 暴力求解
def violence(l = []):
    maxVal = 0
    x,y=0,0
    for i in range(len(l)):
        for j in range(len(l)):
            res = sum(l[i:j])
            if res > maxVal:
                maxVal = res
                x = i
                y = j-1
    return maxVal,x,y

maxVal, x, y = violence(l)

print(maxVal,(x,y))