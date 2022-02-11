class Stack():
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)



def postfixEval(postfixExpr):# 传入的是字符串 类似于 A B * C D * +
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:

        if token in '0123456789':
            operandStack.push(int(token))

        else:# 如果是操作符的话
            operand_one = operandStack.pop()
            operand_two = operandStack.pop()
            result = doMath(token,operand_one,operand_two)
            operandStack.push(result)
    return operandStack.pop()



def doMath(op,op1,op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('4 5 6 * +'))