
'''
# 需求:中缀表达式转换为后缀表达式

- 构造 Stack()  
    - 其核心: 次序反转
- 构造功能函数
'''

class Stack(): # 这是一个关于栈的数据结构
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):# 删除最后一个
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

def infixToPostfix(formula):
    # 首先定义优先级
    priority = {}
    priority['*'] = 3
    priority['/'] = 3
    priority['+'] = 2
    priority['-'] = 2
    priority['('] = 1

    # 存储字符串
    posStack = Stack()
    posfixList = []
    # 分割字符串
    tokenList = formula.split()

    for token in tokenList: # 进行循环遍历
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789": #  存储到tokenList
            posfixList.append(token)
        elif token == '(': # 这个时候进行的操作是入栈
            posStack.push(token)
        elif token == ')': # 这个时候进行的操作是 => 填充.遇到(就停止
            topToken = posStack.pop()
            while topToken != '(':
                posfixList.append(topToken)
                topToken = posStack.pop()
        else: # 如果是计算符号的话
            while (not posStack.isEmpty()) and (priority[posStack.peek()]>=priority[token]): # 2>1
                posfixList.append(posStack.pop())
            posStack.push(token)#1<2
    
    while not posStack.isEmpty():
        posfixList.append(posStack.pop())
    
    return ''.join(posfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


