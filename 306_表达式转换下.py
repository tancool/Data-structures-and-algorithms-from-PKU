'''
- 通用的中缀转后缀算法


- a*b + c*d => 转换为后缀表达式
    - 输出a
    - *入栈
    - 输出b
    - +准备入栈,碰到了乘法=> 优先级没有*高 =>先把乘法输出 => 再把自己入到栈里面去
    - 碰到了c,c直接输出
    - *准备入栈 => +比*的优先级来的低 =>不做任何处理 => *直接入栈
    - d => 输出d
    - 这个时候栈里还有运算符 => 把运算符弹出来输出
    - ab*cd*+

    token表示最小单位
'''

class Stack(): # 将末端设置为栈顶/ 这里要加一个括号
    def __init__(self): # self在对象的方法中表示对象本身,如果通过对象调用一个方法,那么对象就会自动成为地一个参数
        self.items = [] # items表示的是一个属性
    def isEmpty(self): # 判断是否为空 => 需要返回一个值
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self): # 取出最后一个元素
        return self.items.pop()
    def peek(self): # 返回顶元素
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []# 运算元素存放的地方
    tokenList = infixexpr.split()# 分割字符串为数组,默认以空格为参数作为分割

    for token in tokenList:

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":# 如果token是运算内容的话
            postfixList.append(token)# 运算元素存放的地方

        elif token == '(':#　如果是（　=>　就会添加到栈里面去
            opStack.push(token)

        elif token == ')':# 如果 ) 的话 =>
            topToken = opStack.pop() # 反复弹出,直到碰到 '(' 
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else:# 如果是操作符号的话
            # 如果prec[opStack.peek()] 是 * 号 而进来的prec[token] 是加号. 那么就会把 * 给去出来. 
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):# 栈中不为空,并且会进行比较优先级
                  postfixList.append(opStack.pop())
            opStack.push(token)# 把加号存里面

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

a = ['a',31,321,31231,312].pop()
print(a)

'''

# --------
a \
=6; # 与js类似
print(a) # 输出结果是6,并无报错
'''