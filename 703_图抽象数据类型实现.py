class Vertext(): # 包含了顶点信息,以及顶点连接边

    def __init__(self,key):#key表示是添加的顶点
        self.id = key
        self.connectedTo = {} # 初始化临接列表

    def addNeighbor(self,nbr,weight=0):# 这个是赋值权重的函数
        self.connectedTo[nbr] = weight

    
    def __str__(self):
        return str(self.id)+ ' connectedTo: '+str([x.id for x in self.connectedTo])
    
    def getConnections(self): #得到这个顶点所连接的其他的所有的顶点 (keys类型是class)
        return self.connectedTo.keys()
    
    def getId(self): # 返回自己的key
        return self.id
    
    def getWeight(self,nbr):#返回所连接ner顶点的权重是多少
        return self.connectedTo[nbr]

'''
Graph包含了所有的顶点
包含了一个主表(临接列表)
'''
class Graph():# 图 => 由顶点所构成的图

    '''
    存储图的方式是用邻接表实现的.

    数据结构: {
                key:Vertext(){
                    self.id = key
                    self.connectedTo{
                        相邻节点类实例 : 权重
                        ..
                        ..
                    }
                }
                ..
                ..
        }


    '''
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
        #print( 6 in g)
        return n in self.vertList
    
    def addEdge(self,f,t,cost=0): # 添加一条边.
        if f not in self.vertList: # 如果没有边,就创建一条边
            nv = self.addVertex(f)
        if t not in self.vertList:# 如果没有边,就创建一条边
            nv = self.addVertex(t)
        
        if cost == 0:# cost == 0 代表是没有传入参数,而使用的默认参数0,即是是无向图
            self.vertList[f].addNeighbor(self.vertList[t],cost) # cost是权重.无向图为0
            self.vertList[t].addNeighbor(self.vertList[f],cost)
        else:#
            self.vertList[f].addNeighbor(self.vertList[t],cost) # cost是权重
        

    def getVertices(self):# 返回图中所有的定点
        return self.vertList.keys()
    
    def __iter__(self): #return => 把顶点一个一个的迭代取出.
        return iter(self.vertList.values())

g = Graph()

# for i in range(6):
#     g.addVertex(i)
# print(g.vertList)

'''
# a = g.vertList[0]
# print(a.connectedTo)
'''




g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

print(g.getVertices())
# vertList = { key :VertextObject}
# VertextObject =  ||key = key, connectedTo = {到达节点:权重}||   => |||| 表示的是权重的意思

# print(g)
for v in g: # 循环类实例 => return ->  g = VertextObject的集合  v = VertextObject
    for w in v.getConnections(): # 获得类实例的connectedTO
        # print(w)
        print("({},{}:{})".format(v.getId(),w.getId(),v.getWeight(w))) ## 为什么会是这样 => 因为这个时候v就是class啊

