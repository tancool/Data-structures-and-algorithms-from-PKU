'''
- 双端队列集成了栈和队列的特性


- deque定义的操作如下：
    - Deque()：创建一个空双端队列
    - addFront(item)：将item加入队首
    - addRear(item)：将item加入队尾
    - removeFront()：从队首移除数据项，返回值为移除的数据项
    - removeRear()：从队尾移除数据项，返回值为移除的数据项
    - isEmpty()：返回deque是否为空
    - size()：返回deque中包含数据项的个数
'''
class Deque():
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def addRear(self,item):
        self.items.insert(0,item)
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

def palchecker(aString):

    chardeque = Deque()

    for i in aString:
        chardeque.addFront(i)
    
    isPalchecker = True

    while chardeque.size() > 1 and isPalchecker:
        fristStr = chardeque.removeFront()
        lastStr = chardeque.removeRear()

        if fristStr != lastStr:
            isPalchecker = False
    
    return isPalchecker

print(palchecker('aba'))
print(palchecker('abac'))
print(palchecker('上海上'))