# 测试代码可运行. 时间: 20200328
import sys
import os
import unittest


'''
阅读此代码需要把图的构成结构给跑通. 
    参见:
使用广度优先遍历进行标记词梯问题.

读取文件:参见.需要下载单词文件.

参见课程:

'''
                
class Vertex: # 添加顶点
    def __init__(self,num):

        self.id = num # 顶点名称
        self.connectedTo = {} # 邻接表

        self.color = 'white' # 颜色.(用于广度优先)
        self.pred = None # 前驱节点(用于广度优先)
        self.disc = 0 # 设置距离(用于广度优先)

        self.dist = sys.maxsize # sys.naxsize 表示最大值
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0): # 设置权重
        self.connectedTo[nbr] = weight
        
    def setColor(self,color): # 颜色(尚未发现=> 白色 / 已经发现 => 灰色 / 完成探索 => 黑色)
        self.color = color
        
    def setDistance(self,d): # 设置距离
        self.dist = d

    def setPred(self,p): # 前驱顶点
        self.pred = p

    def setDiscovery(self,dtime): # 没有用到
        self.disc = dtime
        
    def setFinish(self,ftime):# 没有用到
        self.fin = ftime
        
    def getFinish(self):# 没有用到
        return self.fin
        
    def getDiscovery(self):# 没有用到
        return self.disc
        
    def getPred(self): # 获得上一个节点
        return self.pred
        
    def getDistance(self): # 获取距离
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):# 获取边的权重.(无向图的权重为0)
        return self.connectedTo[nbr]
                
    def __str__(self): # 没用用到.
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self): # 返回节点名称
        return self.id


class Graph: # 添加边
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n): # 获得顶点
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertices
    
    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())



class Queue: # 队列: 使用队列进行遍历. (队首进,队尾出)
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item): # 队首进
        self.items.insert(0,item)

    def dequeue(self): # 队尾出
        return self.items.pop()

    def size(self):
        return len(self.items)




def buildGraph(wordFile): # 创建桶的函数
    d = {}
    g = Graph()    
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g
    


def bfs(g,start): # bfs算法.
    start.setColor('gray')
    start.setDistance(0) # 由于是起始点.所以起始点距离起始点的距离为0
    start.setPred(None) # 设置前驱顶点.起始顶点的前驱节点是为0
    vertQueue = Queue() # 创建一个空队列
    vertQueue.enqueue(start) # 把起始顶点装进空队列里去
  
    while (vertQueue.size() > 0): # 截至条件是队列为空
        currentVert = vertQueue.dequeue() # 取出第一个进行遍历
        for nbr in currentVert.getConnections(): # 获取此节点的所有邻接点
            if (nbr.getColor() == 'white'): # 如果为白色. 就添加进队列
                nbr.setColor('gray') # 同时设置为gray ( 白色代表尚未发现 / 灰色代表已经发现,但是尚未探索 / 黑色代表已经探索 )
                nbr.setDistance(currentVert.getDistance() + 1) # 同时设置距离 / 等于上一个元素的距离 加 1
        
                nbr.setPred(currentVert) # 同时设置此元素的前驱节点
                vertQueue.enqueue(nbr) # 将此节点插入到队列中去

        currentVert.setColor('black') # 设置为黑色.代表已经探索完成
    
    
def traverse(y): # 回溯函数.
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


wordgraph = buildGraph("fourletterwords.txt") # 创建完成的桶

bfs(wordgraph, wordgraph.getVertex('FOOL')) #  把整个列表给遍历完了.

traverse(wordgraph.getVertex('SAGE'))

#traverse(wordgraph.getVertex('COOL'))


'''
实际测试:代码已经跑通.
深度优先比搜索和广度优先搜索换个词是 深度优先遍历和广度优先遍历
'''
