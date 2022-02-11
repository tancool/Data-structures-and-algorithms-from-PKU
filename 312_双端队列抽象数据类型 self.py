'''
- 双端队列集成了栈和队列的特性
    - 但是需要用户自己手动进行控制

- deque定义的操作如下：
    - Deque()：创建一个空双端队列
    - addFront(item)：将item加入队首
    - addRear(item)：将item加入队尾
    - removeFront()：从队首移除数据项，返回值为移除的数据项
    - removeRear()：从队尾移除数据项，返回值为移除的数据项
    - isEmpty()：返回deque是否为空
    - size()：返回deque中包含数据项的个数
'''
class Deque():# 双端队列

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFornt(self,item):#从头部添加
        self.items.insert(0,item)

    def removFront(self):#从头部删除,并且返回删除的值
        return self.items.pop(0)


    def addRear(self,item):#从尾部添加
        self.items.append(item)

    def removeRear(self):#从尾部删除
        return self.items.pop()

    def size(self):# 返回其值
        return len(self.items)

def palchecker(aString): # 判断会文数的函数
    
    palDeque = Deque() # 实例化双端队列
    
    isMatch = True# 是否匹配

    for i in aString:# puth元素
        palDeque.addFornt(i)

    while palDeque.size()>1 and isMatch:# 判断是否匹配
        if palDeque.removFront() != palDeque.removeRear():
            isMatch = False

    return isMatch

print(palchecker('ab1a'))
print(palchecker('abac'))
print(palchecker('上海上'))
