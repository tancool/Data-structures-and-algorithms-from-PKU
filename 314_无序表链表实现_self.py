class Node():
    def __init__(self,initdata):
        self.data = initdata
        self.next = None # 如果不进行设置,默认是None
    def getNext(self):
        return self.next
    def getDate(self):
        return self.data
    def setNext(self,newnext):
        self.next = newnext
    def setData(self,newdata):
        self.data = newdata



class UnorderedList():
    def __init__(self):
        self.head = None

    def add(self,item):
        temp = Node(item)# 添加数据
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current != None: # current 是一个类
            count = count + 1
            current = current.getNext()
        return count 
a = UnorderedList()
a.add(1)
a.add(1)
a.add(1)
a.add(1)

print(a.size())