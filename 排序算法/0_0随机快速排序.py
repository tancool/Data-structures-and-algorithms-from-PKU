import random
def random_quicksort(a,left,right):
    if(left<right):
        mid = random_partition(a,left,right)
        random_quicksort(a,left,mid-1)
        random_quicksort(a,mid+1,right)


def random_partition(a,left,right): 
    t = random.randint(left,right)     #生成[left,right]之间的一个随机数
    a[t],a[right] = a[right],a[t]    
    x = a[right]
    i = left-1                         #初始i指向一个空，保证0到i都小于等于 x
    for j in range(left,right):        #j用来寻找比x小的，找到就和i+1交换，保证i之前的都小于等于x
        if(a[j]<=x):
            i = i+1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[right] = a[right],a[i+1]  #0到i 都小于等于x ,所以x的最终位置就是i+1
    return i+1

exam_list = [8,6,15,14,13]
random_quicksort(exam_list,0,len(exam_list)-1)
print(exam_list)