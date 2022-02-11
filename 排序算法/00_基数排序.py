def RadixSort(arr):
    max_num = max(arr)
    exp = 1
    resval = arr[:]

    while max_num // exp >0:
        output_arr = [0]*len(arr)
        buckets_arr =  [0]*10

        for i in range(len(arr)): # 数据出现的次数装入到桶中
            buckets_arr[(resval[i]//exp)%10] +=1

        # print('数据装入到桶中:',buckets_arr) # 查看桶信息

        for j in range(1,10): # 计算前面的元素出现多少次(包括此元素)
            buckets_arr[j] += buckets_arr[j-1]
        #print('计算前面的元素出现多少次:',buckets_arr) # 查看排序信息

        '''
        reves[k] 是 reves的值
        resval[k]//exp 是 获得当前整数.
        (resval[k]//exp)%10 是 获得当前的余数
        buckets_arr[(resval[k]//exp)%10] 是
        '''
        for k in range(len(resval)-1,-1,-1): # 进行排序
            output_arr[buckets_arr[(resval[k]//exp)%10] - 1] = resval[k] # 第几名.如果是第一名,那么是arr[0],所以需要减去个1
            buckets_arr[(resval[k]//exp)%10] -= 1  # 
        
        resval = output_arr
        exp = exp *10

    return resval

#
# 算法结束.
# ------------------
# 以下是数据测试类,用于测试算法正确性,非排序算法本身函数.
# 可以删除TestDate类,手动填入数据测试.
#
import unittest
import random
class TestData(unittest.TestCase):
    def create_data(self,num_start,num_end,num_length): # 生成整数
        return [random.randint(num_start,num_end) for i in range(num_length)]

    def test_case1(self):
        numlist = self.create_data(1,20,5)

        print('未排序数据:{}'.format(numlist))
        print(RadixSort(numlist))

        print('\n'*1)
    def test_case2(self):
        numlist = self.create_data(99,375,20)

        print('未排序数据:{}'.format(numlist))
        print(RadixSort(numlist))

        print('\n'*1)
    def test_case3(self):
        numlist = self.create_data(1,8888,5)

        print('未排序数据:{}'.format(numlist))
        print(RadixSort(numlist))

        print('\n'*1)

    def test_case4(self): # 基数遇到负数会出现排序错误
        numlist = self.create_data(-122,222,5)

        print('未排序数据:{}'.format(numlist))
        print(RadixSort(numlist))

        print('\n'*1)



if __name__ == "__main__":
    unittest.main() # 调用测试数据