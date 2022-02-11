# 桶排序可以看成是基数排序的升级版,计数排序的一个单位是一个数,而桶排序的一个单位是一个区间

def bucktetSort(numList,bucketNum):
    import math
    if len(numList) <=0:
        return numList

    maxNum = max(numList)
    minNum = min(numList)

    bucketLength = len(numList)-1
    bucketSize = ((maxNum - minNum) / bucketLength)  # 根据桶的数量找到每个桶的取值范围
    buckets = [[] for i in range(bucketLength)]


    for i in range(len(numList)):     # 将各个数分配到各个桶
        # num_bucktes_local界定范围.只要大于第n个桶,就是在第n+1个桶里.所以是向上取整.
        #比如说 numList = [1,40,50,60,200]. 
        num_bucktes_local =math.ceil((numList[i] - minNum) / bucketSize)-1
        if num_bucktes_local<=0: # 最小值是 == -1 的.
            num_bucktes_local = 0
        buckets[num_bucktes_local].append(numList[i])

    # ---可删除---
    print('桶的取值范围是:',bucketSize)
    print('每个桶的藏的宝贝都是:',buckets)
    # ---可删除---


    for i in range(bucketLength):# 桶内排序，可以使用各种排序方法
        buckets[i].sort()
        
    res = []
    for i in range(len(buckets)):# 分别将各个桶内的数提出来，压入结果
        res.extend(buckets[i])
    return res

# ---测试数据---
import unittest
class TestData(unittest.TestCase):
    def test_one(self):
        numlist = [1,50.76,75,150,200,321,321,32,992]
        print(bucktetSort(numlist,5),'\n'*2)
    def test_two(self):
        numlist = [-13,321,43,6,9,99,12]
        print(bucktetSort(numlist,5),'\n'*2)
    def test_three(self):
        numlist = [1,50.76,12,321,54,787,43]
        print(bucktetSort(numlist,5),'\n'*2)
# ---测试数据结束---

if __name__ == "__main__":
    unittest.main() # 调用测试数据