import sys
class Vertex: # 点
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize # distance : 距离
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



class PriorityQueue: # 这是一个优先队列
    def __init__(self):
        self.heapArray = [(0,0)] # (距离,顶点实例)
        self.currentSize = 0

    def buildHeap(self,alist): # 从一个key列表中创建新堆
        self.currentSize = len(alist)
        self.heapArray = [(0,0)]
        for i in alist: # type(i) == tuple
            self.heapArray.append(i)
        i = len(alist) // 2 # 最后子节点的父元素
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
                
    def minChild(self,i): # 返回最小的孩子
        if i*2 > self.currentSize: # 这行代码有点多余..
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

    def decreaseKey(self,val,amt): # val是顶点对象实例 / amt是新的值
        '''
        这个函数的作用 : 
            寻找key,修改key的值.调整优先队列.
        '''
        done = False # 是否完成 : False
        i = 1 # i表示的是节点
        myKey = 0

        while not done and i <= self.currentSize: # 如果没有完成 且 i < 队列个数
            if self.heapArray[i][1] == val: # 如果有队列中的值等于 对象实例
                done = True # 完成/ 退出循环
                myKey = i # mykey等于i的位置
            else:
                i = i + 1

        if myKey > 0: # 如果mykey >0
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1]) # 修改当前值
            self.percUp(myKey) # 执行上浮操作
            
    def __contains__(self,vtx):
        for pair in self.heapArray:
            if pair[1] == vtx:
                return True
        return False

def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap( [(v.getDistance(), v) for v in aGraph] ) # 建堆.  传递参数 : 第一个是距离.第二个是顶点实例化  tuple类型
    
    while not pq.isEmpty(): # 如果最小二叉堆不为空
        
        currentVertex = pq.delMin() # 取出当前最小的. pop操作.

        for nextVertex in currentVertex.getConnections(): # 遍历距离最小的邻接边

            newDistance = currentVertex.getDistance() + currentVertex.getWeight(nextVertex)

            if newDistance < nextVertex.getDistance(): # 如果距离小于已经存在的距离
                nextVertex.setDistance(newDistance)
                nextVertex.setPred(currentVertex)
                pq.decreaseKey(nextVertex, newDistance) # 执行重排 / 引起优先队列的重排
                # 第一个值是 顶点对象实例化 / 第二个值是新的距离

g = Graph()
g.addEdge('u','v',2)
g.addEdge('u','x',1) 
g.addEdge('u','w',5) 
g.addEdge('x','v',2)
g.addEdge('v','w',3)
g.addEdge('x','y',1)
g.addEdge('x','w',3)
g.addEdge('y','w',1)
g.addEdge('y','z',1)
g.addEdge('w','z',5)

dijkstra(g,g.getVertex('u'))


for vertex in g:
    print(vertex.getId() ,'/',vertex.getDistance())



'''
- 顶点的访问由一个优先队列来控制
    - 最初,只有开始顶点 dist 设为 0
    - 随着队列中每个最低dist顶点率先出队
    - 并计算与其临界顶点的权重.会引起堆重排
'''