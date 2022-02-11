def buble_sort(arr):

    for num_now in range(len(arr)-1,0,-1):
        for i in range(num_now):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

def buble_sort1(arr):

    num_now = len(arr)-1
    change = True

    while num_now > 0 and change:
        change = False
        for i in range(num_now):
            if arr[i+1] < arr[i]:
                arr[i+1],arr[i] = arr[i],arr[i+1]
                change = True
        num_now = num_now - 1
    return arr

import unittest
import random
class TestData(unittest.TestCase):
    def create_data(self,num_start,num_end,num_length): # 生成整数
        return [random.randint(num_start,num_end) for i in range(num_length)]

    def test_case1(self):
        numlist = self.create_data(1,20,5)

        print('未排序数据:{}'.format(numlist))
        print(buble_sort(numlist))

        print('\n'*1)
    def test_case2(self):
        numlist = self.create_data(99,375,20)

        print('未排序数据:{}'.format(numlist))
        print(buble_sort(numlist))

        print('\n'*1)
    def test_case3(self):
        numlist = self.create_data(1,8888,5)

        print('未排序数据:{}'.format(numlist))
        print(buble_sort(numlist))

        print('\n'*1)

    def test_case4(self): # 基数遇到负数会出现排序错误
        numlist = self.create_data(-122,222,5)

        print('未排序数据:{}'.format(numlist))
        print(buble_sort1(numlist))

        print('\n'*1)



if __name__ == "__main__":
    unittest.main() # 调用测试数据