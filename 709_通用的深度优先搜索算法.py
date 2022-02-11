import sys
class Vertex: # 点
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None # pred 表示前驱节点
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

    def setPred(self,p): # 设置前驱节点
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self): # 设置发现时间
        return self.disc
        
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
    
    def addEdge(self,f,t,cost=0): # 添加边 (如果此前没有节点,则会添加节点)
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    
    def getVertices(self):
        return list(self.vertices.keys())
        
    def __iter__(self):
        return iter(self.vertices.values())
    
class DFSGraph(Graph): # 继承其类
    def __init__(self):
        super().__init__() # 继承了其方法
        self.time = 0

    def dfs(self): # 深度优先入口
        # self指向的是类的实例化
        for aVertex in self: # self => 其有邻接矩阵的值 / 也就是边
            # print(self)
            aVertex.setColor('white') # 颜色初始化
            aVertex.setPred(-1) # 前驱初始化为空. -1  == 空

        for aVertex in self: # 如果还有未包括的顶点,则建立森林
            if aVertex.getColor() == 'white':
                # print(aVertex.id) # A
                self.dfsvisit(aVertex)
    
    def dfsvisit(self,startVertex):# 执行发现
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex) # 使用递归进行深度优先
        startVertex.setColor('black') # 这里已经设置的黑色
        self.time +=1
        startVertex.setFinish(self.time)


d = DFSGraph()
d.addEdge('A','B')
d.addEdge('A','D')
d.addEdge('B','C')
d.addEdge('B','D')
d.addEdge('D','E')
d.addEdge('E','B')
d.addEdge('E','F')
d.addEdge('F','C')
d.dfs()

for vertex in d:
    print(vertex.getId(),vertex.getDiscovery(),'/',vertex.getFinish())

        