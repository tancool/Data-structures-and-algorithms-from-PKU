# 这个阶乘有助于理解递归
def  cal(num):
    if num>1:
        return num * cal(num-1)
    else:
        return 1

print(cal(3))