'''
- 散列表冲突解决方案

- 如果两个数据项被散列映射到同一个槽，需要一个系统化的方法在散列表中保存第二个数据项，这个过程称为“解决冲突”

- 解决散列冲突成为散列方法中很重要的一
部分。


'''

'''

解决散列的一种方法就是为冲突的数据项再找一个开放的空槽来保存

最简单的就是从冲突的槽开始往后扫描，直到碰到一个空槽.
如果到散列表尾部还未找到，则从首部接着扫描

这种寻找空槽的技术称为“开放定址

向后逐个槽寻找的方法则是开放定址技术中的“线性探测


采用线性探测方法来解决散列冲突的话，
则散列表的查找也遵循同样的规则

如果在散列位置没有找到查找项的话，就必须向
后做顺序查找

直到找到查找项，或者碰到空槽（查找失败）

- 线性探测法的一个缺点是有 聚 集 （clustering）的趋势
    - 即如果同一个槽冲突的数据项较多的话，这些数据项就会在槽附近聚集起来
    - 从而连锁式影响其它数据项的插入。

- 避免聚集的一种方法就是将线性探测扩展，从逐个探测改为跳跃式探测


'''

'''
- 冲突解决方案：再散列rehashing

- 重新寻找空槽的过程可以用一个更为通用的“再散列rehashing”来概括
'''


'''
- 跳跃式探测中，需要注意的是skip的取值
，不能被散列表大小整除，否则会产生周
期，造成很多空槽永远无法探测到

- 一个技巧是，把散列表的大小设为素数，如例子的11
'''



'''
- 除了寻找空槽的开放定址技术之外，另一
种解决散列冲突的方案是将容纳单个数据
项的槽扩展为容纳数据项集合（或者对数
据项链表的引用）

- 这样，散列表中的每个槽就可以容纳多个
数据项，如果有散列冲突发生，只需要简
单地将数据项添加到数据项集合中。

- 查找数据项时则需要查找同一个槽中的整
个集合，当然，随着散列冲突的增加，对
数据项的查找时间也会相应增加。
'''