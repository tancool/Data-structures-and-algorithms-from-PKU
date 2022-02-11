'''
- 列表list是一种简单强大的数据集结构,提供了丰富的操作接口
    - 有的语言需要自己去实现
- 一种数据项按照相对位置存放的数据集特别的，被称为“无序表unordered list”其中数据项只按照存放位置来索引，如第1个、第2个……、最后一个等。
    - （为了简单起见，假设表中不存在重复数据项）



'''

'''

- 无序表的操作如下
    - List()：创建一个空列表
    - add(item)：添加一个数据项到列表中，假设item原先不存在于列表中
    - remove(item)：从列表中移除item，列表被修改，item原先应存在于表中
    - search(item)：在列表中查找item，返回布尔类型值
    - isEmpty()：返回列表是否为空
    - size()：返回列表包含了多少数据项
    - append(item)：添加一个数据项到表末尾，假设item原先不存在于列表中
    - index(item)：返回数据项在表中的位置
    - insert(pos, item)：将数据项插入到位置pos，假设item原先不存在与列表中，同时原列表具有足够多个数据项，能让item占据位置pos
    - pop()：从列表末尾移除数据项，假设原列表至少有1个数据
    - pop(pos)：移除位置为pos的数据项，假设原列表存在位置p
'''

'''
- 为了实现无序表的数据结构,可以采用链接表的方案
    - 每个节点包含两个信息 : 数据项本身 和 指向下一个节点的引用信息
'''
class Node:
    def __init__(self,initadata):
        self.data = initadata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    
    def __init__(self):
        self.head = Node

