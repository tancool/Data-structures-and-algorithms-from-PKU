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
    def __init__(self,rootObj):
        self.key = rootObj # rootObj是根节点的数据项
        self.leftChild = None # 保存左子树的引用
        self.rightChild = None # 保存右子树的引用

    def insertLeft(self,newNode):
        if self.leftChild == None:# 如果下面是空
            self.leftChild = BinaryTree(newNode)
        else:# 如果不为空
            t = BinaryTree(newNode) # t 意为 temp
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            r.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):# 
        self.key = obj
    
    def getRootVal(self):#
        return self.key
    
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

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

def nodeCount(root):
        nodelen = 0
        if root == None:
            return 0    
        else:
            nodelen = 1 + nodeCount(root.leftChild) + nodeCount(root.rightChild)
        return nodelen



r = BinaryTree('a') # 创建根节点

'''
---------------------------------
填充节点 => 填充完毕内容如下图注释所示
---------------------------------
'''

r.insertLeft('b')
r.insertRight('c')




r.getLeftChild().insertLeft('l1')
r.getLeftChild().insertRight('l_r1')
r.getLeftChild().getLeftChild().insertLeft('l2')

r.getRightChild().insertRight('r1')
r.getRightChild().getRightChild().insertRight('r2')
r.getRightChild().getRightChild().getRightChild().insertRight('r3')
# print(r.key)
# print(r.getLeftChild().getRootVal())

print(nodeCount(r))

'''
填充节点结束
-------------------------------
'''


'''
这个树的结构
              a 
          b        c

      l1   l_r1       r1

    l2                   r2

                           r3
'''

# 树的遍历
'''
前序遍历:
    - 根在前，从左往右，一棵树的根永远在左子树前面，左子树又永远在右子树前面
    - 根>坐子树>右子树
'''
#r.preorder()
# print('前序遍历结束') 


'''
中序遍历
    - 根在中，从左往右，一棵树的左子树永远在根前面，根永远在右子树前面
    - 左子树>根>右子树
'''
#r.inorder() 
# print('中序遍历') # 根在中，从左往右，一棵树的左子树永远在根前面，根永远在右子树前面


'''
后序遍历
    - 根在后，从左往右，一棵树的左子树永远在右子树前面，右子树永远在根前面
    - 左子树>右子树>根
'''
#r.preorder()
# print('后序遍历') #　根在后，从左往右，一棵树的左子树永远在右子树前面，右子树永远在根前面



# 统计二叉树中的结点个数
# 统计二叉树中的叶子结点个数；
#统计二叉树中度为 1 的结点个数
# 统计二叉树中度为 2 的结点个数
# 统计二叉树中结点值等于 e 的结点个数；
# 计算二叉树的深度；