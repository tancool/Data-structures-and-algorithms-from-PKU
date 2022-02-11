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




def genLegalMoves(x,y,bdSize): # 获得合法的节点
    retVal = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]

        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            retVal.append( (newX,newY) )
    return retVal
def legalCoord(x,bdSize): # 确认不会走出棋盘
    if x>=0 and x < bdSize:
        return True
    else:
        return False
def postToNodeId(row,col,bdSize): # 生成其ID
    return row*bdSize + col


def knightGraph(bdSize): # 生成节点
    
    ktGraph = Graph()

    for row in range(bdSize):
        for col in range(bdSize):
            nowid = postToNodeId(row,col,bdSize)
            newPosition = genLegalMoves(row,col,bdSize)

            for e in newPosition:
                nid = postToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nowid,nid)
    return ktGraph

# ----创建图完成----
# ---执行代码的回溯---
def knightTourBetter(n,path,u,limit):
    
    u.setColor('gray')
    path.append(u)

    if n < limit:
        nbrList = orderByAvail(u)
        done = False
        i = 0

        while i < len(nbrList) and not done:
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
    
    u.setColor('gray')
    path.append(u)

    if n < limit:
        nbrList = list(u.getConnections())
        done = False
        i = 0

        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1,path,nbrList[i],limit)
            i = i + 1
        
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done




def orderByAvail(n):
    
    retList = []

    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w  in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            retList.append( (c,v) )
    retList.sort(key=lambda x: x[0])
    return [ y[1] for y in retList]
                    



    

kg = knightGraph(5)

thepath = []
start = kg.getVertex(4)
knightTourBetter(0,thepath,start,24)

for v in  thepath:
    print(v.getId())


