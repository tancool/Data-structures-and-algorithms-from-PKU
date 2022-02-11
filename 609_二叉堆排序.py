def big_endian(arr,start,end):# 执行下沉操作
    root=start    
    child=root*2+1
    while child<=end:

        if child+1<=end and arr[child]<arr[child+1]: # 如果右子节点的值大于左子节点
            child+=1       #child = 右子节点

        if arr[root]<arr[child]: # 如果子节点大于父节点.
            arr[root],arr[child]=arr[child],arr[root]     
            root=child                
            child=root*2+1            
        else:               
            break
         
def heap_sort(arr):
    first=len(arr)//2-1 # 3
    for start in range(first,-1,-1): # 构建二叉堆
        # 3 2 1 0 
        big_endian(arr,start,len(arr)-1)

    for end in range(len(arr)-1,0,-1):
        # 5 4 3 2 1 
        arr[0],arr[end]=arr[end],arr[0]
        big_endian(arr,0,end-1)
        print(arr)
    return arr

     
l=[22,3,5,7,23,11]
print(heap_sort(l))