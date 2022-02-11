'''
- 什么是队列(Queue):
    - 新数据的添加在队尾,数据的移除发生在对首. 也就是先进先出.
    - 就像是排队一样
    - 当数据项加入队列，首先出现在队尾，随着队首数据项的移除，它逐渐接近队首。
    - 这种次序安排的原则称为（FIFO:First-infirst-out）先进先出
    - 在生活当中的例子就像是买东西排队一样
        - 还有就像是 打印队列/进程嗲读/键盘缓冲区

- 抽象数据类型(Queue)
    - 是一个有次序的数据集合
    - 数据仅添加到 尾(rear)端
    - 仅从 首(front)端移除
    - 具有先进先出的操作次序
'''

'''
- 抽象数据类型
    - Queue()：创建一个空队列对象，返回值为Queue对象；
    - enqueue(item)：将数据项item添加到队尾，无返回值；
    - dequeue()：从队首移除数据项，返回值为队首数据项，队列被修改；
    - isEmpty()：测试是否空队列，返回值为布尔值
    - size()：返回队列中数据项的个数。
'''

# 代码实现
# front是入口/rear是出口

class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)# insert object before index
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

a = Queue()
print(a.isEmpty())
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.items)
b = a.dequeue()
print(a.items)