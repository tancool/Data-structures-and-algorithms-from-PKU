
class Vertext():#包含了顶点信息,以及顶点连接边
    def __init__(self,key):
        self.id = key#key表示是添加的顶点
        self.connectedTo = {}#初始化临接列表
        self.range = 0
    def addNeighbor(self,nbr,weight=0):#这个是赋值权重的函数
        self.connectedTo[nbr] = weight#有向图的权重为其权重。如果是0,则是无向图
        self.color = 'white' # 白色：为访问/灰色：准备访问/黑色:已经访问 => 用于广度优先便利
    def __str__(self):
        return str(self.id)+ ' connectedTo: '+str([x.id for x in self.connectedTo])
    def getConnections(self): #得到这个顶点所连接的其他的所有的顶点 (keys类型是class)
        return self.connectedTo.keys()
    def getId(self): # 返回自己的节点
        return self.id
    def getWeight(self,nbr):#返回所连接ner顶点的权重是多少
        return self.connectedTo[nbr]
    def getDistance(self):#获得其距离
        return self.range
    def setDistance(self,size):# 设其距离
        self.range = size
    def getColor(self):#获取颜色
        return self.color
    def setColor(self,iscolor):#设置其颜色
        self.color = iscolor

'''
Graph包含了所有的顶点信息
'''
class Graph():# 图 => 由顶点所构成的图
    def __init__(self):
        self.vertList = {} # 临接列表
        self.numVertices = 0 # 顶点个数初始化
    def addVertex(self,key):# 添加顶点
        self.numVertices = self.numVertices + 1 # 顶点个数累加
        newVertex = Vertext(key) # 创建一个顶点的临接矩阵
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self,n):# 通过key查找定点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):# transition:包含 => 返回所查询顶点是否存在于图中
        return n in self.vertList
    def addEdge(self,f,t,cost=0): # 添加一条边.
        if f not in self.vertList: # 如果没有边,就创建一条边
            nv = self.addVertex(f)
        if t not in self.vertList:# 如果没有边,就创建一条边
            nv = self.addVertex(t)
        if cost == 0:# cost == 0 代表是没有传入参数,而使用的默认参数0,即是是无向图
            self.vertList[f].addNeighbor(self.vertList[t],cost) # cost是权重.无向图为0
            self.vertList[t].addNeighbor(self.vertList[f],cost)
        else:
            self.vertList[f].addNeighbor(self.vertList[t],cost) # cost是权重
    def getVertices(self):# 返回图中所有的定点
        return self.vertList.keys()
    def __iter__(self): #return => 把顶点一个一个的迭代取出.
        return iter(self.vertList.values())
    

g = Graph()



g.addEdge(1,2) 
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(2,4)



class Queue(): # 队列 => 先进先出
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)




# 广度优先遍历 (bfs)
def bfs(g,start):# (图,开始结点)
    viewVertext = [start.getId()]
    start.setDistance(0)# 设置从起始节点到此节点的路径长度
    vertQueue = Queue()# 设置栈,用来存储队列
    vertQueue.enqueue(start)# 把起始点添加到队列里面去

    while (vertQueue.size() > 0): # 进行遍历
        currentVert = vertQueue.dequeue()#取队首作为当前节点

        for nbr in currentVert.getConnections(): # 获得与之相连的节点
            if (nbr.getColor() == 'white'): # 如果此节点是白色(默认没有访问)
                viewVertext.append(nbr.getId()) # 
                nbr.setColor('gray') # 设置为灰色
                nbr.setDistance(currentVert.getDistance() + 1) # 并且距离+1
                vertQueue.enqueue(nbr) # 添加到栈里面去
        currentVert.setColor('black') # 设置为黑色
    return (viewVertext)

bfsResult = bfs(g,g.vertList[4]) 
print(bfsResult)

# 深度优先遍历(dfs)
class DFSGraph(Graph):# 为了不污染原有的数据,继承自Graph.
    '''
    user:tancool
    help:This is a deep traversal class
    Function:
        def dfs() => Initializing the contents of a node
        def dfsvisit() => Access node content
    '''
    def __init__(self):
        super().__init__()
        self.viewVertext = []

    def dfs(self):# 添加颜色函数
        for aVertex in self: # 颜色初始化
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:# 如果还有未包括的定点,则建森林
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex): # 进行对比函数
        self.viewVertext.append(startVertex.getId()) # 添加进行深度遍历的初始节点
        startVertex.setColor('gray') # 设置为gray.表示访问过.但是没有从此节点回去
        for nextVertex in startVertex.getConnections(): #进行遍历
            if nextVertex.getColor() == 'white': # 深度优先递归访问
                self.dfsvisit(nextVertex)
                self.viewVertext.append(nextVertex.getId()) # 添加深度遍历的行走节点

        startVertex.setColor('black') # 设置为黑色,表示已经访问过.已经回去了

        # self.viewVertext.append('~')# 回归节点,已注释
        return self.viewVertext

b = DFSGraph() # 初始化
b.dfs()
b.addEdge(1,2) # 添加边 (如若两点没有在图中,则会先进行添加两点.然后再添加边)
b.addEdge(1,3)
b.addEdge(2,3)
b.addEdge(2,4)

dfsresult = b.dfsvisit(b.vertList[4])
print(dfsresult)
help(DFSGraph())