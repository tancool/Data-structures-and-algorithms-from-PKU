a = [1,2,3,4,5,6]
a.pop(0) # 这个是删除第一个

'''
- pop()从列表末尾移除元素，O(1)
- pop(i)从列表中部移除元素，O(n)

从中部移除元素的话，要把移除元素后面的元素全部向前挪位复制一遍，
这个看起来有点笨拙但这种实现方法能够保证列表按索引取值和赋值的操作很快，
达到O(1)这也算是一种对常用和不常用操作的折衷
'''

import timeit

x = list(range(200000))
popend = timeit.Timer('x.pop()','from __main__ import x')
popzero = timeit.Timer('x.pop(0)','from __main__ import x')

print('time is {}'.format(popend.timeit(100000)))
print('time is {}'.format(popzero.timeit(100000)))