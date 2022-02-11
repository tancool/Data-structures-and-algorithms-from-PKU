class Student1():
    def __init__(self,name):
        self._name = name

    def __gt__(self,obj):
        print('哈哈,{}比{}大吗'.format(self,obj))
        return self._name > obj._name

stu1 = Student1(1) #进行比较的时候，自动触发函数
stu2 = Student1(2)

print(stu1>stu2)
# class Car():
#     def __init__(self,carname,oilcp100km, price):
#         self.carname,self.oilcp100km,self.price = carname,oilcp100km, price

#     def __gt__(self,other):
#         print(self.price,other.price)
#         return self.price>other.price

   
# car1,car2,car3,car4 = Car('爱丽舍',8,10),Car('凯美瑞',7,27),Car('爱丽舍',8,10),Car('途观',12,27)
# print(car1>car2) # car1 = 8 / car2 = 27

