
class Stack(): # 将末端设置为栈顶/ 这里要加一个括号
    def __init__(self): # self在对象的方法中表示对象本身,如果通过对象调用一个方法,那么对象就会自动成为地一个参数
        self.items = [] # items表示的是一个属性
    def isEmpty(self): # 判断是否为空 => 需要返回一个值
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)



def divideby2(decNumber):

    remstack = Stack()

    while decNumber>0:
        rem = decNumber%2
        remstack.push(rem)
        decNumber = decNumber//2 # 这个是整除的意思
    
    binString = ''
    while not remstack.isEmpty():
        print(remstack.items)
        print(remstack.isEmpty())

        binString = binString + str(remstack.pop())
    
    return binString

def dividebyany(decNumber,base):
    import string
    remstack = Stack()

    while decNumber>0:
        rem = decNumber%base
        remstack.push(rem)
        decNumber = decNumber//base # 这个是整除的意思
    
    binString = ''
    while not remstack.isEmpty():
        binString = binString + string.digits[remstack.pop()] # 注意看这里
    
    return binString

print(dividebyany(22,2))
