class Queue():
    '''
    队列
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)

'''
模拟：打印机

主要模拟步骤

创建打印任务的队列，每个任务都有个时间戳。队列启动的时候为空。
每秒（currentSecond）：

是否创建新的打印任务？如果是，将 currentSecond 作为时间戳添加到队列。
如果打印机不忙并且有任务在等待
从打印机队列中删除一个任务并将其分配给打印机
从 currentSecond 中减去时间戳，以计算该任务的等待时间。
将该任务的等待时间附件到列表中稍后处理。
根据打印任务的页数，确定需要多少时间。
打印机需要一秒打印，所以得从该任务的所需的等待时间减去一秒。
如果任务已经完成，换句话说，所需的时间已经达到零，打印机空闲。
模拟完成后，从生成的等待时间列表中计算平均等待时间。
'''
