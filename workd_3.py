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
    

r = BinaryTree('a') # 创建根节点

'''
============================
填充节点 => 填充完毕内容如下图注释所示
============================
'''

r.insertLeft('b')
r.insertRight('c')

r.getLeftChild().insertLeft('l1')
r.getLeftChild().insertRight('l_r1')
r.getLeftChild().getLeftChild().insertLeft('l2')

r.getRightChild().insertRight('r1')
r.getRightChild().getRightChild().insertRight('r2')
r.getRightChild().getRightChild().getRightChild().insertRight('e')

'''
填充节点结束
============================
'''


'''
树的结构
              a 
          b        c

      l1   l_r1       r1

    l2                   r2

                           e
                              
'''


# 树的遍历
'''
============================
前序遍历:
    - 根在前，从左往右，一棵树的根永远在左子树前面，左子树又永远在右子树前面
    - 根>坐子树>右子树
============================
'''
print('------------')
print('前序遍历开始') 
r.preorder()
print('前序遍历结束')
print('------------') 


'''
============================
结束
============================

'''

'''
============================
中序遍历
    - 根在中，从左往右，一棵树的左子树永远在根前面，根永远在右子树前面
    - 左子树>根>右子树
============================
'''
print('------------')
print('中序遍历开始') 
r.inorder() 
print('中序遍历结束') # 根在中，从左往右，一棵树的左子树永远在根前面，根永远在右子树前面
print('------------')

'''
============================
结束
============================

'''


'''
============================
后序遍历
    - 根在后，从左往右，一棵树的左子树永远在右子树前面，右子树永远在根前面
    - 左子树>右子树>根
============================
'''
print('------------')
print('后续遍历开始')
r.preorder()
print('后序遍历结束') #　根在后，从左往右，一棵树的左子树永远在右子树前面，右子树永远在根前面
print('------------')

'''
============================
结束
============================

'''

'''
============================
# 统计二叉树中的结点个数
============================
'''
def nodeCount(root):
        nodelen = 0
        if root == None:
            return 0
        else:
            nodelen = 1 + nodeCount(root.leftChild) + nodeCount(root.rightChild)
        return nodelen

print('------------')
print('统计二叉树的结点开始')
print(nodeCount(r)) # 输出结果是9
print('统计二叉树的节点结束')
print('------------')

'''
============================
结束
============================

'''


'''
============================
# 统计二叉树中的叶子结点个数；
============================
'''
def nodeLeafCount(root):
        nodeLeaflen = 0
        if root == None:
            return 0
        elif root.leftChild == None and root.leftChild == None :
            
            return 1
        else:
            nodeLeaflen = nodeLeafCount(root.leftChild) + nodeLeafCount(root.rightChild)
        return nodeLeaflen
print('------------')
print('统计二叉树的子结点开始')
print(nodeLeafCount(r)) # 输出结果为 3
print('统计二叉树的子结点结束')
print('------------')
'''
============================
结束
============================

'''


'''
============================
# 统计二叉树中度为 1 的结点个数
    - 度数:子结点的个数
============================
'''



nodeOne = 0
def nodeDegForOne(root):
        if root == None: # 如果这个节点是空的话
            return 0
        else:# 如果这个节点不为空
            nodeOne =  nodeDegForOne(root.leftChild) + nodeDegForOne(root.rightChild)
            if (root.leftChild == None and root.rightChild) or (root.leftChild  and root.rightChild == None):
                nodeOne = nodeOne+1
        return nodeOne
print('------------')
print('统计二叉树中度为 1 的结点个数开始')
print(nodeDegForOne(r))
print('统计二叉树中度为 1 的结点个数结束')
print('------------')

'''
============================
统计结束
============================
'''

'''
============================
统计二叉树中度为 2 的结点个数
============================
'''
nodeTwo = 0
def nodeDegForTwo(root):
        if root == None: # 如果这个节点是空的话
            return 0
        else:# 如果这个节点不为空
            nodeTwo = nodeDegForTwo(root.leftChild) + nodeDegForTwo(root.rightChild)
            if (root.leftChild and root.rightChild):
                nodeTwo = nodeTwo+1
        return nodeTwo

print('------------')
print('统计二叉树中度为 1 的结点个数开始')
print(nodeDegForTwo(r))
print('统计二叉树中度为 1 的结点个数结束')
print('------------')

'''
============================
统计结束
============================
'''

'''
============================
# 统计二叉树中结点值等于 e 的结点个数；
    - 代码同二叉树类中的前序遍历,但是在遍历的同时,收集了其遍历值.
============================
'''
finCountE = 0
def findE(root,res = []):
        res.append(root.key)
        if root.leftChild:
            findE(root.leftChild)
        if root.rightChild:
            findE(root.rightChild)
        return res

findEArr = findE(r)
for i in findEArr:
    if i == 'e':
        finCountE = finCountE+1

print('------------')
print('统计二叉树中度为 1 的结点个数开始')
print(finCountE) # 出现次数为一次
print('统计二叉树中度为 1 的结点个数结束')
print('------------')
'''
============================
统计结束
============================
'''


'''
============================
# 计算二叉树的深度；
============================
'''

def CauTreeDeep(root):
    if root is None:
        return 0
    dl = CauTreeDeep(root.leftChild)
    dr = CauTreeDeep(root.rightChild)
    return max(dl, dr) + 1
p = CauTreeDeep(r)

print('------------')
print('统计的深度开始')
print(p) # 输出为5
print('统计的深度结束')
print('------------')

'''
============================
# 计算结束
============================
'''
