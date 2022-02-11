'''

- 动态规划
    - 把问题分解为若干个子问题.
    - 主问题的最优解包含了更小规模子问题的最优解.
    - 以空间换时间.

- 动态规划
    - 从最简单情况开始到达所需找零的循环
    - 其每一步都依靠以前的最优解来得到本步骤的最
优解，直到得到答案。
'''


def dpMakeChange (coinValueList,change,minCoins): # 兼容爱尔波尼亚的21分硬币

    # 从1分开始到change逐个计算最少硬币数

    for cents in range (1,change + 1 ): # [1 ~ 63]  循环63次
        
        # 1.初始化一个最大值
        coinCount = cents # coinCount == 硬币的数量.求最小值的时候,先赋予一个最大值.

        # 2.减去每个硬币,向后查最少硬币数,同时记录总的最少数.
        for j in [c for c in coinValueList if c <= cents]:

            if minCoins[cents - j] + 1 < coinCount: # min_coins[cents - i] + 1 表示的是当前的次数
                coinCount = minCoins[cents - j] + 1

        # 3.得到当前最少硬币数,记录到表中.
        minCoins[cents] = coinCount
    # 返回结果
    # return minCoins
    return minCoins[change]

print(dpMakeChange([1,5,10,25],63,[0]*64))




# 动态规划并且打印出硬币的组合
def dp_make_change(coin_value_list, change, min_coins, coins_used): # min_coins 记录的是需要多少个硬币.

    for cents in range(1,change+1):
        coin_count = cents

        new_coin = 1 # 初始化新加硬币

        for j in [c for c in coin_value_list if c <= cents]:

            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents-j]+1

                new_coin = j  # 对应最小数量所减的硬币

        min_coins[cents] = coin_count

        coins_used[cents] = new_coin # 记录本步骤加的一个硬币 (加的硬币是最优的.)

    print(coins_used)
    return min_coins[change]
 
 
def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin

# print(dp_make_change([1,5,10,25],63,[0]*64,[0]*64))



a_mnt = 63
c_list = [1, 5, 10,25]
c_used = [0] * (a_mnt+1)
c_count = [0] * (a_mnt+1)

print("===========动态规划实现========================")
print('Making change for ', a_mnt, 'requires')
print(dp_make_change(c_list, a_mnt, c_count, c_used), 'coins')
print("They are: ")
print_coins(c_used, a_mnt)
print("The used list is as follows: ")