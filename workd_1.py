'''
#　线性表
- 已知线性表La和Lb中的数据元素按值非递减有序排列,现要求将La和Lb归并为一个新的线性表Lc.且Lc的数据元素扔按值非递减进行有序排列
例如: 
    La = [1,2,3,4,5] Lb = [2,4,6,8,10]
    Lc = [1,2,2,3,4,5,6,8,10]




'''
class Stack(): # 创建一个线性表的类
    def __init__(self): # 构造函数,初始化线性表
        self.items = []
    def user_push(self,item): # 尾部追加元素
        self.items.append(item)
    def user_delete(self,index): # 删除指定下标志的元素
        return self.items.pop(index)
    def user_pop(self):# 删除尾部元素
        return self.items.pop()
    def user_peek(self):# 返回尾部元素
        return self.items(len(self.items)-1)
    def user_isEmpty(self): # 判断线性表是否为空
        return self.items == []
    def user_size(): # 返回线性表的长度
        return len(self.items)
    def user_sort(self): # 对线性表进行排序
        self.items.sort()


def returnList(items): # 元素添加到线性表并且排序,返回排序好的线性表
    create_list = Stack() # 创建线性表类实例
    for i in items: # push元素进入线性表
        create_list.user_push(int(i))
    create_list.user_sort() # 对线性表进行排序

    return create_list.items

def addElem(str): # 填充单个线性表
    num = str.split()
    return returnList(num)
    

def fuseStack(list_1,list_2): # 两个现行表合并为一个新的线性表
    list_1.extend(list_2)
    return returnList(list_1)





La = addElem('1 2 3 4 5')
Lb = addElem('2 4 6 8 10')
Lc =fuseStack(La,Lb)
#print(Lc) # 输出结果 : [1,2,2,3,4,4,5,6,8,10]
print('La为:{}'.format(La))
print('Lb为:{}'.format(Lb))
print('Lc(输出结果)为:{}'.format(Lc))

'''
测试数据
La = addStack('1 2 3 4 5')
Lb = addStack('2 4 6 8 10')
Lc    => [1,2,2,3,4,4,5,6,8,10]
'''