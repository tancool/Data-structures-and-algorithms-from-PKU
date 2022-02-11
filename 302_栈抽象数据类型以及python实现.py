'''
- 栈 Stack
    - 一种有次序的数据项集合.
    - 在栈中，数据项的加入和移除都仅发生在同一端
    - 这一端叫栈“顶top”，另一端叫栈“底base”
    - 例如日常生活中的成叠的盘子
- 距离栈底越近的数据项，留在栈中的时间就越长,而最新加入栈的数据项会被最先移除
    - 这种次序通常称为"后进先出LIFO" Last in frist out
    - 这是一种基于数据项保存时间的次序，时间的离栈顶越近而时间越长的离栈底越近    

- 栈的特性
    - 反转次序
'''

'''
- 栈的抽象数据类型定义
    - Stack()：创建一个空栈，不包含任何数据项
    - push(item)：将item加入栈顶，无返回值
    - pop()：将栈顶数据项移除，并返回，栈被修改
    - peek()：“窥视”栈顶数据项，返回栈顶的数据项但不移除，栈不被修改
    - isEmpty()：返回栈是否为空栈
    - size()：返回栈中有多少个数据项

'''

class Stack(): # 将末端设置为栈顶/ 这里要加一个括号
    def __init__(self): # self在对象的方法中表示对象本身,如果通过对象调用一个方法,那么对象就会自动成为地一个参数
        self.items = [] # items表示的是一个属性
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

a = Stack()
a.push(1)
a.push('das')
a.push('dasd')
a.push('rew')

print(a.size())





