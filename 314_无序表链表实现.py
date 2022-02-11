'''
- 无序表的链表实现


- add
    - 添加方式最快捷的方式是在表头这里(由列表的结构知道,查找列表中的数据都是从表头开始查找的.所以添加方式最好是从head开始)
        - 从表头开始添加数据
        - 新数据项可以加入到原表的任何位置
        - 按照实现的性能考虑，应添加到最容易加入的位置上。
        - head 始终指向的是第一个引用
'''

'''
- 添加方式是颠倒的

 1
 2 1
 3 2 1 
 4 3 2 1 
 5 4 3 2 1 
 6 5 4 3 2 1 
'''


class Node():# 设置节点的类
    def __init__(self,initdata):
        self.data = initdata
        self.next = None#self.next指向下一个节点的下标

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext

class UnorderedList():
    
    def __init__(self):
        self.head = None # 无序表的head始终指向地一个头节点

    def add(self,item): # add方法的实现
        temp = Node(item) # item是数据 / temp是一个对象
        # print(type(temp))  # temp is class
        temp.setNext(self.head)# 设置下一个节点
        self.head = temp #这里的链表头就是上一个对象 / 这里的 = 表示的是引用

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count
    
    def search(self,item):
        
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        return found
    
    def remove(self,item):
    
        '''
        这里采用的是断链的方式进行的操作
        '''
        current = self.head
        previous = None
        found = False # 找到的标志符

        while not found:
            if current.getData() == item:#如果找到
                found = True
            else:# 没有找到
                previous = current
                current = current.getNext()

        if previous == None:#如果在第一个就找到的话
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def isEmpty(self):
        pass

    def append(self):
        pass
    def index(self):
        pass
    def insert(self):
        pass
    def pop(self):
        pass
    def pop(self,pos):
        pass
    def showAll(self):
        returnList = []
        current = self.head # 这个是第一个元素

        while current != None:
            returnList.append(current.getData())
            current = current.getNext()
        return returnList

        
a = UnorderedList()
a.add(1)
a.add(2)
a.add(3)
print(a.size())
print(a.showAll())