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





class DFSGraphStrongConnect(Graph): # 强连通分支类.继承自Graph
    def __init__(self):
        super().__init__() # 继承父元素的属性和类
        self.time = 0 # 表示步骤


    def dfs(self): # 执行深度优先
        for v in self:
            v.setColor('white')
            v.setPred(None)
        lst = list(self.vertices.values())
        lst.sort(key=lambda v:v.finishTime,reverse=True) # 降序排序

        mydict = {}

        for v in lst:
            if v.getColor() == 'white': # 
                mydict[v.getId()] = []
                self.dfsvisit(v,mydict[v.getId()])

        return mydict

    def dfsvisit(self, startV,path): # 深度优先
        path.append(startV)
        startV.setColor('gray')
        self.time += 1
        startV.setDiscovery(self.time)

        for nbr in startV.getConnections():
            if nbr.getColor() == 'white':
                nbr.setPred(startV)
                self.dfsvisit(nbr,path)

        startV.setColor('black')
        self.time += 1
        startV.setFinish(self.time)

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

    g.dfs() # 执行深度优先
    for vertex in g:
        print(vertex.getId(),vertex.getDiscovery(),vertex.getFinish())


    
# -------------------------以上是深度优先-----------------------------

    gt = DFSGraphStrongConnect() # 实例化

    # for node in g:
    #     print(node)
    
    #-------------------------转置开始---------------------
    for node in g: # 遍历深度优先的函数. 遍历节点
        for nbr in node.connectedTo.keys(): # 遍历邻接表

            gt.addEdge(nbr.getId(),node.getId()) # 添加边(反向添加)

            start = gt.getVertex(nbr.getId()) # 如果此节点存在.返回此节点
            start.discoveryTime = nbr.discoveryTime # 发现时间不变
            start.finishTime = nbr.finishTime # 完成时间不变

            end = gt.getVertex(node.getId()) # 判断此节点是否存在
            end.discoveryTime = node.discoveryTime # 赋值发现时间
            end.finishTime = node.finishTime # 赋值完成时间
    #------------------------转置结束-------------------------

    print('-'*70)

    for node in gt:
        print(node.getId(),node.getDiscovery(),node.getFinish())

    print('-' * 70)

    mydict = gt.dfs()

    for node in gt: # 转置后深度搜索之后的值
        print(node.getId(),node.getDiscovery(),node.getFinish())

    print('-' * 70)

    for key,item in mydict.items():
        for node in item:
            print(node.getId(), end=' ')
        print()




# 由于是图的简单应用.不做代码演示.

'''

- 强连通分支的好处:使用强连通分支简化的图,使得简化的图和原图在很多方面都有相同的性质.但是数据量大大的减少
 
'''


'''
- 第一步 : 运行DFS算法
- 第二步 : 转置 : 将所有边的定点交换次序.比如将(v,w)切换为(w,v).
(代码想法已通,但是未编写代码)
- 第三步 : 转置代码运行DFS

'''


'''
这是分析代码.自己写的是self.
'''