# print(28//5) 向下取整

def toStr(num,base): # 十进制转换任意进制
    coverString = '0123456789ABCDEF'
    if num<base:
        return coverString[num]
    else:
        return toStr(num//base,base) + coverString[num%base] # 这个就是栈的应用

print(toStr(5,2))
