
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


def parChecker(symbolString):
    
    s = Stack()
    index = 0
    balance = True

    while index<len(symbolString) and balance:
        
        symbo = symbolString[index]

        if symbo == '(':
            s.push(symbo)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
        index = index+1;
    if s.isEmpty() and balance:
        return True
    else:
        return False

print(parChecker('((()))'))

# 下面的一段代码可以适配更多的括号

def parCheckers(symbolString):
    
    s = Stack()
    index = 0
    balance = True

    while index<len(symbolString) and balance:
        
        symbol = symbolString[index]

        if symbol in'([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balance = False
        index = index+1;
    if s.isEmpty() and balance:
        return True
    else:
        return False

def matches(open,close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

print(parCheckers('[[[[[((({{{((()){{}})}}})))]]]]]'))