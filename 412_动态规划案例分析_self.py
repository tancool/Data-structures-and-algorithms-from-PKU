
'''
w 表示重量
v 表示价值
'''
tr = [
    None,
    {'w':2,'v':3},
    {'w':3,'v':4},
    {'w':4,'v':8},
    {'w':5,'v':8},
    {'w':9,'v':10},
]

# 大强=盗最大承重
max_w = 20


'''
i表示前i件.
w表示重量.
'''
# 初始化二维表格m[(i,w)]
m = {(i,w): 0 for i in range(len(tr)) for w in range(max_w+1)} # type == dict


# 逐个填写二维表格
for i in range(1,len(tr)): # i表示的是前i件
    for w in range(1,max_w+1): # 最大重量的限制
        if tr[i]['w'] > w : # 装不下第i个宝物.
        # tr[i]['w'] 表示的是 第i行的物品所需的重量.w表示当前可以容纳重量.
        # 如果当前可以容纳的重量小于第i行物品所需要的重量.那么跳到第三个条件
            m[(i,w)] = m[(i-1),w]
        
        else:
            m[(i,w)] = max( m[(i-1,w)],m[ (i-1,w-tr[i]['w']) ]+tr[i]['v'] )

print(m [ (len(tr)-1,max_w )])


'''
动态规划的思路是从最底开始计算的.所以会是前i件.
每一个问题的解都依赖于之前问题的解.

'''