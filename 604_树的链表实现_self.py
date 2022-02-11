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
    def __init__(self,root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insertLeft(self,left_obj):

        if self.left_child:
            
            template_obj = BinaryTree(left_obj)
            template_obj.left_child = self.left_child
            self.left_child = template_obj
        else:
            self.left_child = BinaryTree(left_obj)

    def insertRight(self,right_child):
        if self.right_child:
            template_obj = BinaryTree(right_child)
            template_obj.right_child = self.right_child
            self.right_child = template_obj
        else:
            self.right_child = BinaryTree(right_child)

    def getLeftChild(self):
        return self.left_child

    def getRightChild(self):
        return self.right_child

    def SetRootVal(self,key):
        self.key = key

    def getRootVal(self):
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