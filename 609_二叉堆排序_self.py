def percDown(arr,start_node,end_node): # 堆下沉函数
    root_node = start_node
    child_node = root_node*2 + 1 # 左子节点

    while child_node <= end_node:

        if child_node + 1 <=end_node and arr[child_node+1] > arr[child_node]: # 如果右子节点大于左子节点.父节点往比较到大的子节点进行下沉
            child_node = child_node + 1
        
        if arr[child_node] > arr[root_node]:
            arr[root_node],arr[child_node] = arr[child_node],arr[root_node]
            root_node = child_node
            child_node = child_node + 1
        else:
            break

def heap_sort(arr): # 堆排序
    father_node_last = len(arr)// 2 - 1

    for father_node_now in range(father_node_last,-1,-1):
        percDown(arr,father_node_now,len(arr)-1)
    
    for end_node in range(len(arr)-1,0,-1):

        arr[0],arr[end_node] = arr[end_node],arr[0]
        percDown(arr,0,end_node-1)
    return arr

l=[22,3,5,7,23,11]
print(heap_sort(l))