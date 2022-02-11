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

    def getVertexAll(self): # 这个是自己添加的方法.用于返回所有的顶点集合
        return list(self.vertices.values())


class DFSGraph(Graph): # 继承其类
    def __init__(self):
        super().__init__() # 继承了其方法
        self.time = 0

    def dfs(self): # 深度优先
        # self指向的是类的实例化
        for aVertex in self: # self => 其有邻接矩阵的值 / 也就是边
            # print(self)
            aVertex.setColor('white') # 颜色初始化
            aVertex.setPred(-1)

        for aVertex in self: # 如果还有未包括的顶点,则建立森林
            if aVertex.getColor() == 'white':
                # print(aVertex.id) # A
                self.dfsvisit(aVertex)
    
    def dfsvisit(self,startVertex):# 执行发现
        startVertex.setColor('gray')
        self.time += 1 # 发现时间
        startVertex.setDiscovery(self.time)

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black') # 这里已经设置的黑色
        self.time +=1
        startVertex.setFinish(self.time)

class DFSGraphStrongConnect(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0 

    def dfs(self):
        for vertex in self:
            vertex.setColor('white')
            vertex.setPred(-1)

        forest_save = {}
        sort_lst = self.getVertexAll()
        sort_lst.sort(key=lambda v: v.getFinish(),reverse=True)

        for vertex_now in sort_lst:
            if vertex_now.getColor() == 'white':
                forest_save[vertex_now.getId()] = []
                self.dfsvisit(vertex_now,forest_save[vertex_now.getId()])
        return forest_save



    def dfsvisit(self,start_vertex,path):

        self.time += 1

        path.append(start_vertex)

        start_vertex.setColor('gray')
        start_vertex.setDiscovery(self.time)

        for vertex_nbr in start_vertex.getConnections():
            if vertex_nbr.getColor() == 'white':
                vertex_nbr.setPred(start_vertex)
                self.dfsvisit(vertex_nbr,path)
        
        start_vertex.setColor('black')
        self.time += 1
        start_vertex.setFinish(self.time)

if __name__ == '__main__':
    g = DFSGraph() # 深度优先的类实例
    g.addEdge('A','B')
    g.addEdge('B', 'E')
    g.addEdge('B', 'C')
    g.addEdge('E', 'A')
    g.addEdge('E', 'D')
    g.addEdge('D', 'B')
    g.addEdge('C', 'F')
    g.addEdge('D', 'G')
    g.addEdge('G', 'E')
    g.addEdge('F', 'H')
    g.addEdge('H', 'I')
    g.addEdge('I', 'F')
    g.dfs()


    print('*'*70)
    for vertex in g:
        print(vertex.getId(),vertex.getDiscovery(),vertex.getFinish())

    gsc = DFSGraphStrongConnect()
    


    # 转置
    for vertex in g:
        for vertext_nbr in vertex.getConnections():

            gsc.addEdge(vertext_nbr.getId(),vertex.getId())

            transpositon_start = gsc.getVertex(vertext_nbr.getId())
            transpositon_start.setDiscovery(vertext_nbr.getDiscovery())
            transpositon_start.setFinish(vertext_nbr.getFinish())

            transpositon_end = gsc.getVertex(vertex.getId())
            transpositon_end.setDiscovery(vertex.getDiscovery())
            transpositon_end.setFinish(vertex.getFinish())

    # 执行dfs
    ret_list = gsc.dfs()

    print('*'*70)
    for node in gsc: # 转置后深度搜索之后的值
        print(node.getId(),node.getDiscovery(),node.getFinish())

    print('*'*70)
    for key,item in ret_list.items():
        for vertex in item:
            print(vertex.getId(),end=' ')
        print()

    


