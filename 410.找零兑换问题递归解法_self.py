
'''
# 最初的形式
def recMc(coin_value_list,input_coin):
    best_choose = input_coin

    if input_coin in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c<input_coin]:
            now_best_choose = 1 + recMc(coin_value_list,input_coin - i)

            if now_best_choose < best_choose:
                best_choose = now_best_choose
    return best_choose

print(recMc([1,5,10],8))
'''

# 优化版本
def recDc(cion_value_list,input_coin,know_results):
    best_choose = input_coin

    if input_coin in cion_value_list:
        know_results[input_coin] = 1
        return 1
    elif know_results[input_coin] > 0:
        return know_results[input_coin]
    else:
        for i in [c for c in cion_value_list if c<input_coin]:

            now_best_choose = 1 + recDc(cion_value_list,input_coin-i,know_results)

            if now_best_choose < best_choose:
                best_choose = now_best_choose
                know_results[input_coin] = best_choose
    return best_choose



print(recDc([1,5,10,25],63,[0]*64))