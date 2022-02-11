# 贪心策略

def get_min_coins(money_value):

    return_list = []

    currency_value = [1,5,10,25,100]
    sorted_currency_value = sorted(currency_value,reverse=True) # 进行颠倒排序.
    # print(sorted_currency_value)

    for now_currency in sorted_currency_value:
        
        len_current_value = money_value//now_currency
        return_list += [now_currency]*len_current_value
        money_value -= len_current_value*now_currency

        if money_value <= 0:
            break
    return return_list


if __name__ == "__main__":
    print(get_min_coins(72))
    #print(int(1.8))