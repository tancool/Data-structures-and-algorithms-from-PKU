
'''
逻辑已通.但是未总结.
代码已抄.但是未分析.
'''

# 宝物的重量和价值
tr = [
    None,
    {'w': 2, 'v': 3},
    {'w': 3, 'v': 4},
    {'w': 4, 'v': 8},
    {'w': 5, 'v': 8},
    {'w': 9, 'v': 10}
]
 
# 大盗最大承重
max_w = 20
 
# 初始化二维表格m[(i, w)]
# 表示前i个宝物中，最大重量w的组合，所得到的的最大价值
# 当i什么都不取，或w上限为0， 价值均为0
m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}

# 逐个填写二维表格
for i in range(1, len(tr)):
    for w in range(1, max_w + 1):
        if tr[i]['w'] > w:  # 装不下第i个宝物
            m[(i, w)] = m[(i - 1), w]
        else:
            # 不装第i个宝物，装第i个宝物，两种情况下最大价值
            m[(i, w)] = max(m[(i - 1, w)], m[(i - 1, w - tr[i]['w'])] + tr[i]['v'])
 
# 输出结果
print(m[(len(tr) - 1, max_w)])



'''
# 递归
# 宝物的重量和价值(这里用set()集合使得tr为不可变类型,还可以用来计算，tuple()的话就不能计算)
tr = {
    (2, 3),
    (3, 4),
    (4, 8),
    (5, 8),
    (9, 10)
}
 
# 大盗最大承重
max_w = 20
 
# 初始化记忆化表格m
# Key是（宝物组合，最大重量），value是最大价值
m = {}
 
 
def theif(tr, w):
    # 情况: 什么都没得选，或者最大负重为0
    if tr == set() or w == 0:
        m[(tuple(tr), w)] = 0  # tuple是key的要求
        return 0  # 返回的最大重量是0
    # 如果表中存在，则直接返回
    elif (tuple(tr), w) in m:
        return m[(tuple(tr), w)]
    # 核心部分
    else:
        vmax = 0
        for t in tr:  # 每个t的都有可能产生最大v_max
            if t[0] <= w:
                # 逐个从集合中去掉某个宝物，递归调用
                # 选出所有价值中的最大值
                v = theif(tr-{t}, w-t[0]) + t[1]
                vmax = max(vmax, v)
        m[(tuple(tr), w)] = vmax
        return vmax
 
 
print(theif(tr, max_w))

'''




# 递归和动态规划的区别