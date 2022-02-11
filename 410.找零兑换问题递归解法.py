# 递归版本
def recMC(coinValueList, change): # change表示的是硬币.
    
    minCoins = change # 最小个数.现在是63个.

    if change in coinValueList: # 终止条件是 如果change等于币值其中的一个的话,return.
        return 1

    else:
        for i in [c for c in coinValueList if c < change]:
            # [] => 小于change的币值组成的数组.
            numCoins = 1 + recMC(coinValueList, change-i)

            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins

print(recMC([1,5,10,25], 8)) # 这个程序执行的太慢了.


'''
coinValueList = [1,5,10,25]
change = 5

for i in [c for c in coinValueList if c>change]: # 先执行中括号里面的代码,返回的是一个满足条件的数组.并且c在循环中是未定义的
    print(i)
'''


# 提高递归效率的方法就是:消除重复计算.
import time
def recDC(coinValueList, change, knownResults):
    # start = time.time()
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoins = 1 + recDC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    # end = time.time()
    # length = end - start
    # print(length)

    return minCoins
    
print(recDC([1,5,10,25], 63,[0]*64)) # len == 64. 但是len[0]不会被调用.这种方法提高了递归的效率.