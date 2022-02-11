import sys
class Vertex: # 点
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id
    
    def addNeighbor(self,nbr,weight=0): # 添加邻接边
        self.connectedTo[nbr] = weight
        
    def setColor(self,color): # 设置颜色
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
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
    
    def getVertex(self,n): # 是否拥有此点
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
                

class Queue: # 队列
    def __init__(self):
        self.items = []

    def isEmpty(self): # 判断是否为空
        return self.items == []

    def enqueue(self, item): # 头部插入
        self.items.insert(0,item)

    def dequeue(self): #  尾部删除
        return self.items.pop()

    def size(self): # 返回队列的大小
        return len(self.items)


def genLegalMoves(x,y,bdSize): # 合法走棋位置函数
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]

    for i in moveOffsets:
        newX = x+i[0]
        newY = y+i[1]

        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    
    return newMoves

def legalCoord(x,bdSize): # 确认不会走出棋盘
    if x>=0 and x < bdSize:
        return True
    else:
        return False


def knightGraph(bdSize):# 构建走棋关系图 (现在是8*8)
    
    '''
    row 和 col 均是从0开始的
    '''

    ktGraph = Graph() # 创建一个图 (邻接表)
    for row in range(bdSize): # 一行
       for col in range(bdSize): # 一列
           nodeId = postToNodeId(row,col,bdSize) # 创建一个id
           newPositions = genLegalMoves(row,col,bdSize) # 返回当前元素可以合法走棋的位置函数
           for e in newPositions:
               nid = postToNodeId(e[0],e[1],bdSize)
               ktGraph.addEdge(nodeId,nid)# 把可以走的棋盘建立起边.
    return ktGraph
        
    

def postToNodeId(row,col,bdSize): # 返回此节点在棋盘的ID.(递增的)
    return row*bdSize + col

# --------创建边结束.开始回溯--------

def knightTourBetter(n,path,u,limit):
    '''
    n:层次/path:路径/u:当前顶点/Limit:搜索总深度
    '''
    u.setColor('gray') # 设置当前节点为灰色
    path.append(u) # 添加到队列里来

    if n<limit:
        nbrList = orderByAvail(u) # u:当前顶点 / orderByAvail
        i = 0
        done = False

        while i<len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1,path,nbrList[i],limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done
    
def knightTour(n,path,u,limit):
    '''
    n:层次/path:路径/u:当前顶点/Limit:搜索总深度
    '''
    u.setColor('gray')
    path.append(u)

    if n <limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False

        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                '''
                递归加回溯 : 见课件.
                '''
                done = knightTour(n+1,path,nbrList[i],limit)
            i = i + 1
        if not done: # 无法完成总深度. 回溯.尝试本层的下一个顶点
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections(): # 输出其邻接边
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections(): # 获得邻接边的元素
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v)) # c表示有多少个遍历的子元素 / v表示子元素
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


kg = knightGraph(5)

thepath = [] # 记录路径


start = kg.getVertex(4) # 获得一个起始点(开始走的起始点)

knightTourBetter(0,thepath,start,24)
for v in thepath:
    print(v.getId())