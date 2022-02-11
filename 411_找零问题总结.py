def get_min_coins(money_value):  # 贪心版本
    '''
    贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。
    也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。
    '''
    return_list = []
    money_coins = [1,5,10,25,100] # 不兼容爱尔波尼亚的21分硬币.其实63的最优解应该是三个21的硬币.贪心算法的局限性
    money_coins_sorted = sorted(money_coins,reverse=True)

    

    for current_value in money_coins_sorted:

        len_current_value = money_value // current_value 
        return_list += [current_value] * len_current_value
        money_value = money_value - current_value*len_current_value
        '''
        第一次: len_current_value == 2 , return_list = [25,25] , money_value ==  13
        第二次: ...
        第三次: ...
        第四次: ...

        '''
        if money_value <=0: # 截至条件
            break
    return return_list

#print(get_min_coins(63))



def recMC(coin_value_list,money_value): # 使用递归求得最优解

    '''
    递归三条件:
        不断缩小自身规模
        不断调用自身
        有结束条件
    其中,递归是自顶向下进行计算的.
    '''
    min_len = money_value
    if money_value in coin_value_list: # 递归结束条件
       return 1
    else:
        for current_value in [c for c in coin_value_list if c < money_value]:
            now_len = 1 + recMC(coin_value_list,money_value-current_value) # 调用自身,且缩小规模
            if now_len < min_len:
                min_len = now_len

    return min_len

# print(recMC([1,5,10,25], 63)) # 这个程序执行的太慢了.一共需要执行67,716,925次.



def recDc(coin_value_list,money_value,know_results): # 递归改进版本
    '''
    递归改进的关键是消除重复计算.其中有一种技术是备忘录技术.

    可以用一个表将计算过的中间结果保存起来，在计算之前查表看看是否已经计算过

    在递归调用之前，先查找表中是否已有部分找零的最优解如果有，
    直接返回最优解而不进行递归调用如果没有，才进行递归调用
    '''
    min_len = money_value
    print(know_results)
    if money_value in coin_value_list:
        return 1
    elif know_results[money_value] !=  0:
        return know_results[money_value]

    else:
        for i in [c for c in coin_value_list if c < money_value]:
            now_len = 1 + recDc(coin_value_list,money_value-i,know_results)

            if now_len < min_len:
                min_len = now_len
                know_results[money_value] = now_len
                print(know_results)
    
    return min_len

# print(recDc([1,5,10,25],63,[0]*64))



def dpMakeChange (coinValueList,change,minCoins): # 动态规划解法
    '''
    动态规划:其所求的最优解是由子问题的最优解构成的.
    
    动态规划是自底向上的计算.

    在找零递加的过程中，设法保持每一分钱的递加都是最优解，一直加到求解找零钱
    数，自然得到最优解
    '''
    for coin in range(1,change+1):
        
        min_len = coin

        for i in [ c for c in coinValueList if c <=coin]:
            if minCoins[coin-i] + 1 < min_len:
                min_len = minCoins[coin-i]+1
        
        minCoins[coin] = min_len
    return minCoins[change]
    

# print(dpMakeChange([1,5,10,25],63,[0]*64))


def dp_make_change(coin_value_list,money_value,minCOins,coins_record):# coins_record记录每一个最优解所添加的硬币.用于返回最优硬币
    '''

    '''
    for coin in range(1,money_value+1):
        
        min_len = coin
        new_add_coin =1

        for i in [c for c in coin_value_list if c <= coin]:
            
            if minCOins[coin-i] + 1 < min_len:
                min_len = minCOins[coin-i] + 1
                new_add_coin = i
        minCOins[coin] = min_len
        coins_record[coin] = new_add_coin
    
    # print(coins_record)
    return minCOins[money_value]

def print_coins(cions_record,how_much_money):
    '''
    在得到最后的解后，减去选择的硬币币值，回溯到表格之前的部分找零，
    就能逐步得到每一步所选择的硬币币值
    '''
    rev_cions = []
    while how_much_money>0:
        how_much_money = how_much_money - cions_record[how_much_money]
        rev_cions.append(cions_record[how_much_money])
    return rev_cions

# some_money = 63
# cions_record = [0]*64
# print(dp_make_change([1,5,10,25],some_money,[0]*64,cions_record))

# print(print_coins(cions_record,some_money))