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
        else:#
            self.vertList[f].addNeighbor(self.vertList[t],cost) # cost是权重
        

    def getVertices(self):# 返回图中所有的定点
        return self.vertList.keys()
    
    def __iter__(self): #return => 把顶点一个一个的迭代取出.
        return iter(self.vertList.values())

'''
g = Graph()
g.addEdge(1,2) 
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(2,4)
for i in g:
    for j in i.getConnections():
        print('{},{},{}'.format(i.getId(),j.getId(),i.getWeight(j)))

'''
'''
import os
print(os.getcwd())
'''


'''
===================
建立边的最直接算法，是对每个顶点（单词），与其它所有单词进行比较，如果相差仅1个字母，则建立一条边时间复杂度是O(n^2)
    - 对于所有4个字母的5110个单词，需要超过2600万次比较

解决办法就是创建大量的桶
    - 桶标记是去掉1个字母，通配符“_”占空的单词


代码分析:
    - 在同一个桶之间相互建边
===================
'''
def buildGraph(wordFile): # 采用字典建立桶
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')


#　创建一个字母不同的字母桶
    for line in wfile:# line是一行的数据
        word = line[:-1]# 这么做为了去掉最后一行的换行符

        for i in range(len(word)):# len(word)=4 => 循环四次
            bucket = word[:i] + '_' + word[i+1:] #进行拼接字符串,若是word[0:0] => 则输出空
            if bucket in d: # 如果bucket已经在字典里了,代表他们去掉一位是相同的=> 那么就把word添加进字典里
                d[bucket].append(word)
            else:# bucket没在字典里,那么把bucket添加进字典里,并且把本身添加到value里.
                d[bucket] = [word] # 重点看这里,创建一个数组

# 在相同的桶中为单词添加顶点和边
    for bucket in d.keys():# bucket => d的key组成的数组
        for word1 in d[bucket]:# 二层遍历
            for word2 in d[bucket]:# 二层遍历
                if word1 != word2:# 如果不相等,就为其添加边
                    g.addEdge(word1,word2)
    return g
# buildGraph('fourletterwords.txt')

# with open(r'fourletterwords.txt','r') as f:
#     # 按行读取内容
#     str_line = f.readline()
#     while str_line:
#         print(str_line)
#         str_line = f.readline()

