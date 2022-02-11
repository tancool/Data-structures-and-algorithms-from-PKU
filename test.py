class Graph():
    def __init__(self):
        self.items = {'a':1,'b':2,'c':3}

    def __str__(self):
        return '打印我干嘛'
    
    def __contains__(self,x): # 判断一个定点是否包含在里面
        return x in self.items
    
    def __iter__(self):
        return iter(self.items)
    



a = Graph()

# print('a' in a) # 通过在类中添加 __contains__ , 可以实现 Class实例化的对象 进行 in 操作 => 输出 True
# print('d' in a) # 通过在类中添加 __contains__ , 可以实现 Class实例化的对象 进行 in 操作 => 输出 False

''''
for i in a:# 通过在类中添加__iter__ , 可以对类实例化的制定可迭代对象进行迭代
    print(i)


c = [1,2,3,4]
it = iter(c)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# print(next(it))
'''
'''
class myrange:
    def __init__(self, start = 0, end = None, step = 1):
        # 判斷參數是否有提供 end，如果沒有提供 end 則 start 為結束值
        # 從 0 跑到 end
        if end == None:
            self.index = 0
            self.start = 0
            self.end = start

        # 三個參數都有提供的話，從 start 跑到 end 為止，每一次遞增 step
        else:
            self.index = start
            self.start = start
            self.end = end

        self.step = step

    def __iter__(self):
        # 當 iter() 呼叫時，會來這裡要一個可走訪的物件
        # 而我們也有 __next__() 方法可以讓人走訪，所以我們回傳 self 
        # 讓 next() 呼叫 self.__next__()
        # 同時代表著，我們也能不做出 __next__() ，而是回傳其他的可走訪物件
        # 像是回傳 [1, 2, 3].__iter__() 一樣也能被 for 迴圈走訪

        return self

    def __next__(self):
        self.index += self.step

        #記得要丟出 StopIteration 例外讓 for 迴圈停止，而這裡只是判斷超出範圍就丟例外
        if self.start < self.end and not self.start < self.index <= self.end:
            raise StopIteration

        elif self.start > self.end and not self.start > self.index >= self.end:
            raise StopIteration

        return self.index

for i in myrange(10):
    print(i)
'''


'''
class ite(): # 这个是关于迭代器的函数/ 其中__iter__() 返回了一个可迭代变量. 可以通过for进行操作对象~
    def __init__(self):
        self.items = [1,2,3,4,5,6]
    def __iter__(self):
        return iter(self.items)


s = ite()

for i in s:
    print(i)

'''


        
print('----------')
a = {}

a[8] = '324'
a[231] = '324'
a[312] = '324'
for i in a:
    print(i)

'''
class Graph():
    def __init__(self):
        self.numVertices = 0
        self.vertList = {顶点1：连接边} # 存储顶点的集合。连接边是 Clall Vertext()的实例化

class Vertext():#包含了顶点信息,以及顶点连接边
    def __init__(self,key):
        self.id = key # key表示的是此顶点
        self.connectedTo = {相连的顶点1：权重,相连的顶点2：权重,相连的顶点3：权重...相连的顶点n：权重}
        self.range = 0 # 点之间的距离

'''
print('hello World')

print('*'*50)


a = [1,2,3,4]
a.append(666)
c = a.pop()
print(a)
print(c)


print('*'*50)

d = {'a':'b','c':'d'}

for i in d:
    print(d[i])
