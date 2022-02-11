class Vertext():
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):

        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connection' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph():# 图 => 由顶点所构成的图
    def __init__(self):
        # 数据结构 (vertList){ key: Vertext{ connectedto{ Vertext:Weight } }  }
        self.numVertices = 0
        self.vertList = {}
 
    
    def addVertex(self,key):# 添加顶点
        self.numVertices = self.numVertices + 1
        new_vertex = Vertext(key)
        self.vertList[key] = new_vertex
        return new_vertex
    
    def getVertex(self,search_key):# 通过key查找顶点
        if search_key in self.vertList:
            return self.vertList[search_key]
        else:
            return None


    def __contains__(self,search_key):# transition:包含 => 返回所查询顶点是否存在于图中
        return search_key in self.vertList

    
    def addEdge(self,s,t,n=0): # 添加一条边.
        if s not in self.vertList:
            nv = self.addVertex(s)
        if t not in self.vertList:
            nv = self.addVertex(t)
        
        if n == 0:
            self.vertList[s].addNeighbor(self.vertList[t],n)
            self.vertList[t].addNeighbor(self.vertList[s],n)
        else:
            self.vertList[s].addNeighbor(self.vertList[t],n)



    def getVertices(self):# 返回图中所有的定点
        return self.vertList.keys()

    def __iter__(self): #return => 把顶点一个一个的迭代取出.
        return iter(self.vertList.values())



g = Graph()

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

