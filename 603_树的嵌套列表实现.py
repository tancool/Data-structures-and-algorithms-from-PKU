'''
           1

       3       2
    4    8  9     7





'''

def BinaryTree(r): # 构造一个仅有根节点的二叉树
    return [r,[],[]]

def insertLeft(root,newBranch): # 将新节点插入树中作为直接的左节点
    t = root.pop(1)#　左子树
    if len(t)>1:
        root.insert(1,[newBranch,t,[]]) # 一颗递归的树/ insertRight也是如此
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def inserRight(root,newBranch): # 将新节点插入树中作为直接的右节点
    t = root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root): # 取得根节点
    return root[0]

def setRootVal(root,newVal): # 
    print(root)
    root[0] = newVal

def getLeftChild(root):# 返回左子树
    return root[1]

def getRightChild(root):# 返回右子树
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
inserRight(r,6)
inserRight(r,7)
# setRootVal(r,432)


l = getLeftChild(r)
print(l)
setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))
'''
c = [5, [4, [], []], []]
[5, [4, [], []], []]
[3, [9, [4, [], []], []], [7, [], [6, [], []]]]
[3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
[6, [], []]
'''