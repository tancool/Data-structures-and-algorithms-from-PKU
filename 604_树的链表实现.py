'''
每一次实现类,都是一颗小树/ 以此递归

'''

'''
# 结构
- BinaryTree()
    - insertLeft()
    - inserRight()
    - getLeftChild()
    - getRightChild()
    - SetRootVal()
    - GetRootVal()
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
    
    def getRootVal(self):#
        return self.key

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getLeftChild().insertLeft('dcc')
r.getLeftChild().insertLeft('dccc')
print(r.getLeftChild().getLeftChild().getRootVal())

print(r.getLeftChild().getRootVal())
print(r.getRootVal())
print(r.getLeftChild().getRootVal())
print(r.getRightChild().getRootVal())
print(r.getLeftChild().getLeftChild().getRootVal())

'''
这个树的结构
              a 
           b     c
      dccc
    dcc
'''