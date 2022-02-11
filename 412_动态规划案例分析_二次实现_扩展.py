# tr = [
#     None,
#     {'w':2,'v':3},
#     {'w':3,'v':4},
#     {'w':4,'v':8},
#     {'w':5,'v':8},
#     {'w':9,'v':10},
# ]

# max_w = 20

# table_dp = {(i,w):0 for i in range( len(tr) ) for w in range(max_w+1)}

# for i in range(1,len(tr)):
#     for w in range(1,max_w+1):
#         if w < tr[i]['w']: 
#             # 如果当前要加入进来的宝物所需的重量绝对大于当前的全部重量.那么就不加入次宝物.
#             # 比如说m(5,5),只能够负担起5的重量,但是仅仅是第五件所需要的重量是9.所以m(5,5) == m(4,5).
#             # 没有办法加进第五件的宝物
#             pass
#             table_dp[ (i,w) ] = table_dp[ (i-1,w) ]
#         else:
#             pass
#             # 再加进一件宝物的最高价值只会有两种.一种是加入宝物,一种是不加入宝物.
#             table_dp[ (i,w) ] = max( table_dp[(i-1,w)] , tr[i]['v']+table_dp[ i-1,w-tr[i]['w'] ] )

# # print(tr[3])
# print(table_dp)
# print(table_dp[(5,20)])



# ---------------------------------以下是扩展模式,可回溯--------------------------------------------------

def museum_robber_dp(tr,max_w,table_dp,table_rec):
    for i in range(1,len(tr)):
        for w in range(max_w+1):
            if tr[i]['w'] > w:
                table_dp[ (i,w) ] = table_dp[ (i-1,w) ]
            else:
                if  tr[i]['v'] + table_dp[ ( i-1,w- tr[i]['w']) ] > table_dp[ (i-1,w) ]:
                    table_dp[ (i,w) ] = tr[i]['v'] + table_dp[ ( i-1,w- tr[i]['w']) ]
                    table_rec[i][w] = 1
                else:
                    table_dp[ (i,w) ] = table_dp[ (i-1,w) ]





def rec_goods(arr,tr,max_w,table_dp):
    '''
    回溯推理:
    最后结果是28
        - 28为1. ?
            - i-1 , v = v - v_i , w = w - w_i
            - 28 不动 , i-1 . w 不动
    截至条件是:判断背包的容量
        - 
    '''

    '''
    max_w 是背包容量
    i 当前选择的哪个物品
    j 当前物品的价值
    '''
    ret_val = []
    i = len(tr) - 1 # 第i件宝物.表格的y轴
    j = max_w # 背包容量.相当与表格的x轴.
    good_val = table_dp[ (i,j) ]

    while good_val>0 and i > 0: # 循环条件是 : 背包里还有东西 且 i 大于 0

        if arr[i][j] == 1:

            j = j - tr[i]['w']
            good_val = good_val - tr[i]['v']
            ret_val.append(i)

        else: # 表示没有选中.不进行任何操作
            pass # 不做任何操作,可删除
        i = i - 1
    return ret_val


if __name__ != "__main__":

    tr = [ # 各种物品的重量与价值
        None,
        {'w':2,'v':3},
        {'w':3,'v':4},
        {'w':4,'v':8},
        {'w':5,'v':8},
        {'w':9,'v':10},
    ]
    max_w =  20 # 最大承重


    # table_dp  : 二维表格(type : dict)
    # table_rec : 回溯数组
    table_dp = {(i,w):0 for i in range(len(tr)) for w in range(max_w+1) }
    table_rec = [[ 0 for i in range( max_w+1)] for j in range(len(tr)) ] # 相当于一个双重循环后面的for循环嵌套在外面 / 如果加入此商品就用1表示,如果没有加默认就是0


    museum_robber_dp(tr,max_w,table_dp,table_rec)

    print(table_dp[ (5,20) ])

    print(table_dp)
    print(table_rec)

    print(rec_goods(table_rec,tr,max_w,table_dp))

# ---------------------------------以上是扩展模式,可回溯--------------------------------------------------



# 递归模式的解法:


def theif(tr, w):
    if tr == set() or w == 0: # 递归结束条件: 集合为空,或者负重为0(已经不能再装东西了)

        '''
        tr == set()这段代码应该有误
        正确的应该是 tr == {}.
        '''
        '''
        tr == set() : tr是一个空集合.
        或者 w(负重) == 0
        {
            ( ( (5, 8), ), 2 ): 0,  ( (5, 8), ) 是一个元组.如果元组里只有一个元组的话,那么默认后面是有一个逗号的
            (((2, 3), (5, 8)), 4): 3, 
            (((3, 4),), 0): 0
        }
        '''
        print(tr == set())
        m[(tuple(tr), w)] = 0
        # print('---')
        # print(m)
        # print('---')
        return 0
        
    elif (tuple(tr), w) in m:
        # print((tuple(tr), w))
        return m[(tuple(tr), w)]

    else:
        vmax = 0
        for t in tr: 
            if t[0] <= w:
                v = theif(tr-{t}, w-t[0]) + t[1] # t1是v
                vmax = max(vmax, v)
        m[(tuple(tr), w)] = vmax
        # print(m)
        return vmax

    

tr = {
    (2, 3),
    (3, 4),
    (4, 8),
    (5, 8),
    (9, 10),
} # (w,v). tr_type = set (集合). 数学中的集合.一堆无序的数据

max_w = 20 # 最大承重
m = {} # 备忘录 type == dict

print(theif(tr, max_w))


print('*'*50)
# m[(tuple( {(2,3)}), 1)] = 555
# print(m)
# tu = {2,2,}

# print(type(tu))
# print((2,3) in tr)
# print(type(m))
# b = (0,)
# print(b)


# seta = {
#     (5,7)
# }
# m = {
# }

# m[ ( tuple(seta),5) ]  = 0
# print(m) 
# {(((5, 7),), 5): 0}

# a = {
#     (5,7)
# }
# b = tuple(a) # 元组里放 集合
# print(b) # ((5, 7),)



#-----------------------------------------------------------

'''
{
    (((5, 8),), 2): 0, 
    (((2, 3), (5, 8)), 4): 3, 
    (((3, 4),), 0): 0, 
    (((3, 4), (2, 3)), 2): 3,
    (((3, 4), (5, 8)), 5): 8, 
    (((3, 4), (5, 8), (2, 3)), 7): 11, 
    (((9, 10),), 6): 0, 
    (((9, 10), (5, 8)), 11): 10,
    (((9, 10), (2, 3)), 8): 3, 
    (((9, 10), (2, 3), (5, 8)), 13): 13,
    (((9, 10), (3, 4)), 9): 10, 
    (((9, 10), (3, 4), (5, 8)), 14): 18, 
    (((9, 10), (3, 4), (2, 3)), 11): 13, 
    (((9, 10), (3, 4), (2, 3), (5, 8)), 16): 21, 
    (((4, 8),), 1): 0, 
    (((5, 8), (4, 8)), 6): 8, 
    (((2, 3), (4, 8)), 3): 3,
    (((2, 3), (5, 8), (4, 8)), 8): 11,
    (((3, 4), (4, 8)), 4): 8, 
    (((3, 4), (5, 8), (4, 8)), 9): 16,
    (((4, 8), (3, 4), (2, 3)), 6): 11, 
    (((3, 4), (2, 3), (5, 8), (4, 8)), 11): 19, 
    (((9, 10), (4, 8)), 10): 10, (((9, 10), (5, 8), (4, 8)), 15): 18,
    (((9, 10), (3, 4), (4, 8)), 13): 18, 
    (((9, 10), (3, 4), (5, 8), (4, 8)), 18): 26, 
    (((9, 10), (2, 3), (4, 8)), 12): 13, 
    (((9, 10), (2, 3), (5, 8), (4, 8)), 17): 21,
    (((9, 10), (3, 4), (2, 3), (4, 8)), 15): 21,
    (((4, 8), (9, 10), (2, 3), (3, 4), (5, 8)), 20): 29
       }
       '''