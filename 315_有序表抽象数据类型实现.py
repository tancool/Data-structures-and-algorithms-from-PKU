class Node():
    def __init__(self,data):
        self.next = None
        self.data = data

    def getData(self):
        return self.data

    def setData(self,data):
        self.data =  data
        
    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next

class UnordererList():
    def __init__(self):
        self.head = None

    def add(self,data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp # 这里的head是一个Object

    def size(self):
        count = 0
        current = self.head

        while current != None:
            count = count+1
            current = current.getNext()
        return count

    def remove(self,deValue):
        find = False
        previous = None
        current = self.head

        while not find:
            if self.head == deValue:#如果在第一次就找到的话
                find = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:# 如果是第一个
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def showAll(self):

        returnList = []
        current = self.head

        while current != Node:
            returnList.append(current.getData())
            current = current.getNext()
a = UnordererList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
print(a.size())
