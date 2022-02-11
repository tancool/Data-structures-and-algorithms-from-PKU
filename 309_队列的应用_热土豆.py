# 代码实现
# front是入口/rear是出口
class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)# insert object before index
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

        
'''
- 约瑟夫问题就是操场丢沙包问题

'''

def hotPotato(nameList,num):
    simqueue = Queue()

    for name in nameList:
        simqueue.enqueue(name)
    
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    
    return simqueue.dequeue()

print(hotPotato(['小明','小红','小刚','小绿','小强','小王','小建','42','42','42','42'],7)) 