
'''

# 问题分析
- 打印机
    - 先到先服务

- 实际配置
    - 一小时内大约有10名学生
    - 每名学生发起2次打印请求
    - 每次是1~20页

- 打印机性能
    - 草稿模式
        - 每分钟10页 (6s/page)
    - 正常模式 
        - 每分钟5页 (12s/page)

- 问题:
    - 怎么设定打印机的模式，让大家都不会等太久的前提下尽量提高打印质量？

'''

'''
#　场景建模

- 对问题进行建模
    -   对象：打印任务、打印队列、打印机
        打印任务的属性：提交时间、打印页数
        打印队列的属性：具有FIFO性质的打印任务队列
        打印机的属性：打印速度、是否忙

- 过程：生成和提交打印任务
    确定生成概率：实例为每小时会有10个学生提交的20个作业，这样，概率是每180秒会有1个作业生成并提交，概率为每秒1/180。
    确定打印页数：实例是1～20页，那么就是1～20页之间概率相同。

- 过程：实施打印
    - 当前的打印作业：正在打印的作业打印结束倒计时：新作业开始打印时开始倒计时，回0表示打印完毕，可以处理下一个作业

- 模拟时间：
    - 统一的时间框架：以最小单位（秒）均匀流逝的时间，设定结束时间
    - 同步所有过程：在一个时间单位里，对生成打印任务和实施打印两个过程各处理一次


'''

'''
# 模拟流程
- 创建打印队列对象

- 时间按照秒的单位流逝

- 按照概率生成打印作业，
    - 加入打印队列如果打印机空闲，且队列不空，则取出队首作业打印，记录此作业等待时间
    - 如果打印机忙，则按照打印速度进行1秒打印如果当前作业打印完成，则打印机进入空闲

- 时间用尽，开始统计平均等待时间


- 作业的等待时间
    - 生成作业时，记录生成的时间戳
    - 开始打印时，当前时间减去生成时间即可
- 作业的打印时间
    - 生成作业时，记录作业的页数
    - 开始打印时，页数除以打印速度即可
'''
class Queue():
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


# 代码实现

import random
# 模拟打印机
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

# 模拟任务
import random

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

#模拟打印机任务队列

import random

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,20) # 3600s 