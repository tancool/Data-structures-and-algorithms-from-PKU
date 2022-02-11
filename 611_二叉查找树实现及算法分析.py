#!/bin/env python3.1
# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005, 2010

'''
Author:  Brad Miller
Date:  1/15/2005
Description:  Imlement a binary search tree with the following interface
              functions:  
              __contains__(y) <==> y in x
              __getitem__(y) <==> x[y]
              __init__()
              __len__() <==> len(x)
              __setitem__(k,v) <==> x[k] = v
              clear()
              get(k)
              items() 
              keys() 
              values()
              put(k,v)
              in
              del <==> 
'''

'''
比父节点小的key都出现在左子树，比父节点大的key都出现在右子树
'''


class BinarySearchTree: # 二叉查找树

    def __init__(self):
        self.root = None # 这个是根节点的成员.引用根节点的treenode
        self.size = 0
    
    def put(self,key,val): # 插入key构建BST.最主要的是key,因为key参加排序
        if self.root: # 调用一个递归函数来放置key(bst是一个递归的数据结构)
            self._put(key,val,self.root)
        else:# 如果BTS为空.那么就自己成为根节点root
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode): # _put是一个递归的函数 / currentNode : 当前的节点
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
            
    def __setitem__(self,k,v): # 这个是索引赋值
        self.put(k,v)
        '''
        test['PKU'] = 100871

        mytree = BinarySearchTree
        mytree[2] = 'red'  => 比如说就可以这样
        mytree[3] = 'pink'
        mytree[4] = 'yellow'
        mytree[5] = 'green'
        '''

    def get(self,key): # 要在bst中找到key所在的节点,然后把数据项给取出来
        if self.root:
            res = self._get(key,self.root) # 如若不是空树,那么就执行递归
            if res:
                return res.payload # 如果找到节点
            else: # 如果没有找到
                return None
        else:# 如果是一个空树
            return None
        
    def _get(self,key,currentNode): #递归函数
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
            
        
    def __getitem__(self,key): # 这个是索引的取值 : 和索引赋值是相对的
        
        '''
        mytree[6] 通过这种方式,把pyload给取出来
        '''

        res = self.get(key)
        if res:
            return res
        else:
            raise KeyError('Error, key not in tree')
            

    def __contains__(self,key): # 实现归属判断 in操作符

        '''
        实现归属判断
        3 in myree
        mytree[6]
        '''

        if self._get(key,self.root):
            return True
        else:
            return False
        
    def length(self): # 包含了了多少个节点
        return self.size

    def __len__(self): # 包含了多少个节点.
        return self.size

    def __iter__(self): # 迭代器
        return self.root.__iter__()
    
    def delete(self,key):# 删除方法
        if self.size > 1: 
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key: #如果只有一个节点
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key): # 删除方法

        '''

        del mytree[3]
        '''
        self.delete(key)
    
    def remove(self,currentNode): 
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,currentNode.leftChild.payload,currentNode.leftChild.leftChild,currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,currentNode.rightChild.payload,currentNode.rightChild.leftChild,currentNode.rightChild.rightChild)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self,tree):
        if tree != None:
            self._inorder(tree.leftChild)
            print(tree.key)
            self._inorder(tree.rightChild)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tree):
        if tree:
            self._postorder(tree.rightChild)
            self._postorder(tree.leftChild)
            print(tree.key)            

    def preorder(self):
        self._preorder(self,self.root)

    def _preorder(self,tree):
        if tree:
            print(tree.key)            
            self._preorder(tree.leftChild)
            self._preorder(tree.rightChild)

                
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None): #
        self.key = key
        self.payload = val # 所包含数据项
        self.leftChild = left # 左子节点
        self.rightChild = right # 右子节点
        self.parent = parent # 方便做回溯
        self.balanceFactor = 0
        
    def hasLeftChild(self): # 是否拥有左子节点
        return self.leftChild

    def hasRightChild(self): # 是否拥拥有右子节点
        return self.rightChild
    
    def isLeftChild(self): # 是否是父节点的左孩子
        return self.parent and self.parent.leftChild == self

    def isRightChild(self): # 是否是父节点的右孩子
        return self.parent and self.parent.rightChild == self

    def isRoot(self): # 判断是否是根节点
        return not self.parent

    def isLeaf(self): # 是否是一个叶节点
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self): # 是否有子节点
        return self.rightChild or self.leftChild

    def hasBothChildren(self): # 是否同时拥有左右子节点
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self,key,value,lc,rc): # 替换子节点
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
        
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ


    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def __iter__(self): # 这个是迭代器 (中序遍历)
        """The standard inorder traversal of a binary tree."""
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
    def inorder(self, currentNode):
           if currentNode.leftChild:
               self.inorder(currentNode.leftChild)
           print(currentNode.key, end=" ")
           if currentNode.rightChild:
               self.inorder(currentNode.rightChild)
            
def testBst():
    # [70,31,93,94,14,23,73] 顺序插入:
    bst = BinarySearchTree()
    bst.put(70, "first")
    bst.put(31, "second")
    bst.put(93, "third")
    bst.put(94, "fourth")
    bst.put(14, "fifth")
    bst.put(23, "sixth")
    bst.put(73, "seventh")
    print(bst.length())
    print(bst.get(14))
    for item in bst:
        print(item, end=" ")
    bst.delete(70)
    print()
    for item in bst:
        print(item, end=" ")
    print()
    bst.inorder()

testBst()