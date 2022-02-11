'''

- 完全二叉树:完全二叉树，叶节点最多只出现在最底层和次底层，
而且最底层的叶节点都连续集中在最左边，每个内部节点都有两个子节点，最多可有1个节点例外
'''

class BinHeap(): # 二叉堆 (创建一个空二叉堆对象)

    # 采用一个列表来保存堆数据，其中表首下标为0的项无用，但为了后面代码可以用到简单的整数乘除法，仍保留它。
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def percUp(self,i): # 这个是上浮的代码
        while i // 2 > 0: # 如果还有父元素
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k): # 将新key插入到堆中.(上浮)
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i): # 下沉
        while (i*2) <= self.currentSize: # 如果子节点存在.
            mc = self.minChild(i) # 返回子节点的下标位置
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i): # 返回最小的子元素
        # 选择较小的子节点交换下沉
        if i*2+1 > self.currentSize: # 唯一的子节点
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]: # 返回较小的
                return i*2
            else:
                return i*2 + 1
    


    def delMin(self): # 返回堆中最小项,同时从堆中删除

        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize] # 将最后一个元素添加到头部
        self.currentSize = self.currentSize - 1
        self.heapList.pop() # 删除最后一个元素
        self.percDown(1) # 进行下沉操作
        return retval # 返回第一个数字
    
    def buildHeap(self,alist): # 从一个key列表创建新堆
        i = len(alist) // 2 # 从最后节点的父节点开始,因为叶节点无需下沉. (i表示最后一个元素的父节点)
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        
        # print(len(self.heapList),i)

        while (i>0):
            print(self.heapList,i)
            self.percDown(i)
            i = i -1
        print(self.heapList,i)

bh = BinHeap()
# bh.insert(5)
# bh.insert(7)
# bh.insert(3)
# bh.insert(11)

# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())

bh.buildHeap([22,3,5,7,23,11])

print(bh.currentSize)
for i in range(bh.currentSize):
    print(bh.delMin(),end=' ')
    print(bh.heapList)
# 使用非嵌套列表来实现


# p*2 == 左子元素. p*2+1 == 右子元素 p//2 等于父元素

# “下沉”路径的选择：如果比子节点大，那么选择较小的子节点交换下沉.



'''
Readme:
老师授课内容是:608是二叉堆的理论部分 / 609是二叉堆的代码实现. / 二叉堆排序是扩展内容

对应到代码文件: 608是二叉堆的代码实现 / 609是二叉堆排序
2020/04/11
'''