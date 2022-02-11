'''
# 树的结构: 非线性的特征.
- 前序遍历(递归):根 左 右
- 中序遍历(递归): 左 根 右
- 后序遍历(递归): 左 右 根
'''
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
    
    def getRootVal(self):
        return self.key


    # ------------递归函数--------------

    def preoder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preoder()
        if self.rightChild:
            self.rightChild.preoder()
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)


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



r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getLeftChild().insertLeft('dcc')
r.getLeftChild().insertLeft('dccc')



'''
这个树的结构
              a 
           b     c
      dccc
    dcc
'''

preorder(r)									#前序遍历树
print('前序遍历结束')
inorder(r)										#中序遍历树
print('中序遍历结束')
postorder(r) 									#后序遍历树


'''

可以用后序遍历法重写表达式代码

'''

'''
中序遍历算法.
'''