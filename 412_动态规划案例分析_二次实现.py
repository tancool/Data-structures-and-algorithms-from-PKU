
def museum_robber_dp(table,max_w):

    table_dp = {(i,w):0 for i in range(len(tr)) for w in range(max_w+1)} # 构建表. 纵向 i 是个数,横向 w 是重量 table_dp 类型是dict
    for i in range(1,len(tr)):
        for w in range(1,max_w+1):

            if w < tr[i]['w']: # 如果二维表格中,前i个,横向w重量绝对小于第i个的重量. 那么 m(i,w) = m(i-1,w)
                '''
                如果第i件商品的重量比当前重量还要重的话,那么就去找上个的解
                '''
                table_dp[(i,w)] = table_dp[(i-1,w)]
            else:
                '''

                '''
                table_dp[ (i,w) ] = max(table_dp[i-1,w],tr[i]['v']+table_dp[i-1,w-tr[i]['w']]) # 加上第i个宝物,背包的容量减少,但是价值增加.
    
    return table_dp

tr = [
    None,
    {'w':2,'v':3},
    {'w':3,'v':4},
    {'w':4,'v':8},
    {'w':5,'v':8},
    {'w':9,'v':10},
]

max_w = 20 # 最大重量

result_list_dp = museum_robber_dp(tr,max_w)
print(result_list_dp) # 完整的表格
print(result_list_dp[ ( len(tr)-1,max_w) ] )  # 返回所求的最优值


'''
关于对动态规划的理解:
    动态规划是自底向上进行求解的.也就是从最简单的问题开始求解.且子问题的解都是最优解.子问题一点一点的增加,最后到所求问题.在这过程之中,每个问题的解都是最优解.
    我在理解背包问题的时候习惯直接从结果去凑.这样是不理解动态规划以及构造的二维表格.
    背包问题可以理解为 : 子问题到所求问题的最优解.其中一些前i件到多少重量都是为了后面的计算而做的支持.
'''