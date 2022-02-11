def BinaryTree(root_value):
    return [root_value,[],[]]

def insertLeft(root,new_branch):
    template = root.pop(1)
    if len(template) > 1:
        root.insert(1,[new_branch,template,[]])
    else:
        root.insert(1,[new_branch,[],[]])

def insertRight(root,new_branch):
    template = root.pop(2)
    if len(template) > 1:
        root.insert(2,[new_branch,[],template])
    else:
        root.insert(2,[new_branch,[],[]])

def getRootValue(root):
    return root[0]

def setRootValue(root,new_branch):
    root[0] = new_branch
    


def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)

l = getLeftChild(r)
print(l)
setRootValue(l,9)
print(r)
insertLeft(l,11)

print(str(r) == '[3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]') # 通过输出,代码与原结果是一样的.


print(getRightChild(getRightChild(r)))