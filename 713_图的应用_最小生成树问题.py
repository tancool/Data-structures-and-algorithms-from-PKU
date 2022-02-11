

import sys
class Vertex: # 点
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None # pred 表示前驱节点
        self.discoveryTime = 0 # !! 这个变量名修改了. (发现时间)
        self.finishTime = 0 # !! 这个变量名修改了 (完成时间)

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0): # 添加邻接边
        self.connectedTo[nbr] = weight
        
    def setColor(self,color): # 设置颜色
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p): # 设置前驱节点
        self.pred = p

    def setDiscovery(self,dtime):
        self.discoveryTime = dtime
        
    def setFinish(self,ftime):
        self.finishTime = ftime
        
    def getFinish(self):
        return self.finishTime
        
    def getDiscovery(self): # 设置发现时间
        return self.discoveryTime
        
    def getPred(self): # 获得前驱节点
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self): # 设置颜色
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.discoveryTime) + ":fin " + str(self.finishTime) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id


class Graph: # 图
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        
    def addVertex(self,key): # 添加边
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex
    
    def getVertex(self,n): # 此节点是否存在
        if n in self.vertices: # 遍历的是key
            return self.vertices[n] # 如果存在,返回节点内容
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



class PriorityQueue: # 这是一个二叉堆
    def __init__(self):
        self.heapArray = [(0,0)]
        self.currentSize = 0

    def buildHeap(self,alist):
        self.currentSize = len(alist)
        self.heapArray = [(0,0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2            
        while (i > 0):
            self.percDown(i)
            i = i - 1
                        
    def percDown(self,i): # 下沉代码
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc
                
    def minChild(self,i):
        if i*2 > self.currentSize:
            return -1
        else:
            if i*2 + 1 > self.currentSize:
                return i*2
            else:
                if self.heapArray[i*2][0] < self.heapArray[i*2+1][0]:
                    return i*2
                else:
                    return i*2+1

    def percUp(self,i): # 上浮代码
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i//2][0]:
               tmp = self.heapArray[i//2]
               self.heapArray[i//2] = self.heapArray[i]
               self.heapArray[i] = tmp
            i = i//2
 
    def add(self,k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def decreaseKey(self,val,amt):
        # this is a little wierd, but we need to find the heap thing to decrease by
        # looking at its value
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1])
            self.percUp(myKey)
            
    def __contains__(self,vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False

def prim(aGraph, start): # 普林姆算法 (优先队列中.最小的始终是在最前面的.之前不理解的地方卡在里这里.从剩余优先队列中选择最小的)
    # 每次选择的边都是 : 可以添加的边的所有选择中最小的那个
    pq = PriorityQueue()
    '''
    // 这段代码是多余的.初始化的状态并未发生改变
    for v in aGraph:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    '''
    start.setDistance(0) # 设置起始点的距离是0
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])

    while not pq.isEmpty():
        currentVertex = pq.delMin() # 每次都是最小的
        # 贪心策略
        for nextVertex in currentVertex.getConnections(): # 获得所有的邻接边
            newCost = currentVertex.getWeight(nextVertex) # 获得邻接边的权重
            if nextVertex in pq and newCost < nextVertex.getDistance(): # !! 这个判断是重点 如果 邻接边在优先队列里 且 邻接边的权重小于顶点已经存在的权重
                
                nextVertex.setPred(currentVertex) # 设置前驱

                nextVertex.setDistance(newCost + currentVertex.getDistance()) # 设置距离
                pq.decreaseKey(nextVertex, newCost) # 重排

def traverse(targetVertex): # 回溯
    x = targetVertex
    while (x.getPred()):
        print(x.getId(), end=" <- ")
        x = x.getPred()
    print(x.getId())
    
def buildRouteGraph():# 这是有向带权图
    g = Graph()
    g.addEdge("A", "B", 2)
    g.addEdge("A", "C", 3)
    g.addEdge("B", "C", 1)

    g.addEdge("B", "D", 1)
    g.addEdge("B", "E", 4)
    g.addEdge("D", "E", 1)

    g.addEdge("E", "F", 1)
    g.addEdge("C", "F", 5)
    g.addEdge("F", "G", 1)
    return g

graph1 = buildRouteGraph()
prim(graph1, graph1.getVertex("A"))
print("prim后 源路由器 A 到目标路由器 G 的最佳路径是: ", end=" ")
traverse(graph1.getVertex('G'))


'''
最小生成树 就是 : 最小权重生成树

对应老师的图.c连接的是b

使用优先队列进行模拟
'''

