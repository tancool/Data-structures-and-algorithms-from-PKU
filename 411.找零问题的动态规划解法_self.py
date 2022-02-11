'''
- 动态规划
    - 把一个主问题分解为一些子问题.
    - 子问题是最佳解.
    - 以空间换取时间
'''

def dpMakeChange(coin_value_list,input_coin_value,min_coin_list):

    for cents in range(1,input_coin_value+1):
        min_coin_count = cents

        for j in [c for c in coin_value_list if c <= cents]:

            if min_coin_list[cents - j] + 1 < min_coin_count:
                min_coin_count = min_coin_list[cents - j] + 1

        min_coin_list[cents] = min_coin_count
    
    return min_coin_list[input_coin_value]


print(dpMakeChange([1,5,10,25],63,[0]*64))