'''
递归三要素
    - 基本结束条件
    - 缩小规模
    - 调用自身
'''
# 解析树生成函数
class BinaryTree():

    def __init__(self,rootObj): # 树的初始化
        
        self.key = rootObj # rootObj是根节点的数据项
        self.leftChild = None # 保存左子树的引用
        self.rightChild = None # 保存右子树的引用

    def insertLeft(self,newNode):
        print(self.leftChild)

        if self.leftChild == None:# 如果下面是空
            self.leftChild = BinaryTree(newNode)
        else:# 如果不为空
            t = BinaryTree(newNode) # t 意为 template
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):# 
        self.key = obj
    
    def getRootVal(self):#
        return self.key

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


def buildParseTree(fpexp): # 生成树
	fplist = fpexp.split()								
	pStack = Stack()									
	eTree = BinaryTree('')								
	pStack.push(eTree)									
	currentTree = eTree 								
	for i in fplist:									
		if i == '(':									
			currentTree.insertLeft('')					
			pStack.push(currentTree)					
			currentTree = currentTree.getLeftChild()	
		elif i not in ['+', '-', '*', '/', ')']:		
			currentTree.setRootVal(int(i))				
			currentTree = pStack.pop() 					
		elif i in ['+', '-', '*', '/']:					
			currentTree.setRootVal(i)					
			currentTree.insertRight('')					
			pStack.push(currentTree)					
			currentTree = currentTree.getRightChild()	
		elif i == ')':									
			currentTree = pStack.pop()					
		else:
			raise ValueError 							
	return eTree


import operator


def evaluate(parseTree): # 递归树(实际上是一个后序遍历)
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	leftC = parseTree.getLeftChild()			
	rightC = parseTree.getRightChild()

	if leftC and rightC:
		fn = opers[parseTree.getRootVal()] # 操作类型
		return fn(evaluate(leftC),evaluate(rightC))	

	else:	
		return parseTree.getRootVal()		


'''
 # 前序遍历函数
 def preorder(tree):
 	if tree:									#若树不为None，则
 		print(tree.getRootVal())				#打印根节点值
 		preorder(tree.getLeftChild())			#前序遍历左子树
 		preorder(tree.getRightChild())			#前序遍历右子树
 # 中序遍历函数
 def inorder(tree):
 	if tree:									#若树不为None，则
 		inorder(tree.getLeftChild())			#中序遍历左子树
 		print(tree.getRootVal())				#打印根节点值
 		inorder(tree.getRightChild())			#中序遍历右子树
 # 后序遍历函数
 def postorder(tree):
 	if tree:									#若树不为None，则
 		postorder(tree.getLeftChild())			#后序遍历左子树
 		postorder(tree.getRightChild())			#后序遍历右子树
 		print(tree.getRootVal())				#打印根节点值
'''
pt = buildParseTree("( ( 10 + 4 ) * 3 )")
print(evaluate(pt))