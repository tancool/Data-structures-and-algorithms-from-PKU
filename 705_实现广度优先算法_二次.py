# 测试代码可运行. 时间: 20200328
import sys
import os
import unittest


                
class Vertex: # 添加顶点
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}

        self.color = 'white' # 颜色
        self.dist = sys.maxsize # sys.naxsize 表示最大值
        self.pred = None # 前驱节点
        self.disc = 0 # 设置距离
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color): # 颜色(尚未发现=> 白色 / 已经发现 => 灰色 / 完成探索 => 黑色)
        self.color = color
        
    def setDistance(self,d): # 设置距离
        self.dist = d

    def setPred(self,p): # 前驱顶点
        self.pred = p

    def setDiscovery(self,dtime): # 这个还不知道是干吗用的
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self): # 还有这个现在也不知道是干嘛用的
        return self.disc
        
    def getPred(self): # 获得上一个节点
        return self.pred
        
    def getDistance(self): # 获取距离
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
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
    

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,val):
        self.items.insert(0,val)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    
wordgraph = buildGraph("fourletterwords.txt") # 创建完成的桶


def bfs(g,start):
    start.setColor('gray')
    start.setDistance(0)
    start.setPred(None)

    vertQueue = Queue()
    vertQueue.enqueue(start)

    while (vertQueue.size() > 0):

        currentValue = vertQueue.dequeue()
        # print(currentValue)

        for nbr in currentValue.getConnections():

            if (nbr.getColor() == 'white'):
                
                nbr.setColor('gray')
                nbr.setDistance( currentValue.getDistance() + 1 )
                nbr.setPred( currentValue )
                vertQueue.enqueue(nbr)

        currentValue.setColor('black')


def traverse(y):
    x = y
    while x.getPred():
        print(y.getId())
        x = x.getPred()
    print(x.getId())


    

wordgraph = buildGraph("fourletterwords.txt") # 创建完成的桶

bfs(wordgraph, wordgraph.getVertex('FOOL')) #  把整个列表给遍历完了.
traverse(wordgraph.getVertex('SAGE'))
'''
 执行广度优先
    - 有颜色判断
'''