'''
- list类型各种操作（interface）的实现方法有很多，如何选择具体哪种实现方法？
    - 总的方案就是，让最常用的操作性能最好，牺牲不太常用的操作
        - 80/20准则：80%的功能其使用率只有20%
'''

def test1():
    l = []
    for i in range(1000):
        l = l +[i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)] # => 这个是列表生成式

def test4():
    l = list(range(1000))


from timeit import Timer

t1 = Timer("test1()",'from __main__ import test1')
print('concat的执行时间是:{} s.'.format(t1.timeit(number=1000)))

t2 = Timer("test2()",'from __main__ import test2')
print('append的执行时间是:{} s.'.format(t2.timeit(number=1000)))

t3 = Timer("test3()",'from __main__ import test3')
print('列表生成式的执行时间是:{} s.'.format(t3.timeit(number=1000)))

t4 = Timer("test4()",'from __main__ import test4')
print('list的执行时间是:{} s.'.format(t4.timeit(number=1000)))

'''
最优的时间排序: t4>t3>t2>t1
'''