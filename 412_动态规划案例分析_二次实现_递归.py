def theif(tr,w):
    if tr == {} or w == 0:
        m[ (tuple(tr),w)] = 0
        return 0
    elif (tuple(tr),w) in m :
        return  m[ (tuple(tr),w) ]
    else:
        vmax = 0
        for t in tr:
            if t[0] <= w:
                v = theif(tr-{t},w-t[0]) + t[1]
                vmax = max(vmax,v)
        m[(tuple(tr),w)] = vmax
        return vmax
            

'''
找到三个元素,画一下就明白了
20200225

当作树来进行理解.就容易进行理解
'''


tr = { # { () } = 字典 里装 tuple
    (2,3),
    (3,4),
    (4,8),
    (5,8),
    (9,10),
}
max_w = 20
m = {}

print(theif(tr,max_w))
