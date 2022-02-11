# 这个是最大堆: 只需要改变上浮与下沉的交换条件就可以

class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def percUp(self,i): # 这个是上浮的代码
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2


    def insert(self,key):
        self.heapList.append(key)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        # print(self.currentSize,'--')
        
    
    def maxChild(self,i):
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2+1] > self.heapList[i*2]:
                return i*2 +1
            else:
                return i*2
        

    def perdown(self,i):

        while i*2 <= self.currentSize: # 如果子元素存在
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tep = self.heapList[i]
                self.heapList[i] =  self.heapList[mc]
                self.heapList[mc] = tep
            i = mc
        

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()

        self.perdown(1)

        return retval
    
    def buildHeap(self,alist):
        
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        i = len(alist)//2

        while i>=1:
            self.perdown(i) # 执行下沉操作
            i = i - 1


bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)
bh.insert(21)
bh.insert(101)
bh.insert(31)


print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

bh.buildHeap([22,3,5,7,23,11])
print(bh.heapList)