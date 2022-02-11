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
        else: # 无向图
            self.vertList[f].addNeighbor(self.vertList[t],cost) # cost是权重
        

    def getVertices(self):# 返回图中所有的定点
        return self.vertList.keys()
    
    def __iter__(self): #return => 把顶点一个一个的迭代取出.
        return iter(self.vertList.values())



def buildGraph(file_name):

    d = {}
    f = open(file_name,'r')
    g = Graph()
    
    for line in f:
        now_word = line[:-1]
        print(now_word)

        for i in range(len(now_word)):
            bucket = now_word[:i] + '_' + now_word[i+1:]

            if bucket in d:
                d[bucket].append(now_word)
            else:
                d[bucket] = [now_word]
    
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)

    f.close()
    return g

a = buildGraph('fourletterwords.txt')
print(1)
