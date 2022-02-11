import turtle

t = turtle.Turtle()
'''
t.forward(100)
'''
'''
for i in range(4): # 正方形
    t.forward(100)
    t.right(90)
turtle.done()
'''

'''
# 五角星
t.pencolor('red')
t.pensize(3)
for i in range(5):
    t.forward(100)
    t.right(144)
turtle.done()
'''
'''
# 递归螺线
def drawSpiral(t,lineLen):
    if lineLen>0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t,lineLen-5)

drawSpiral(t,500)
turtle.done()

'''
'''
# 罗斌老师 在这里讲到了分形学
#   - 部分和整体相似
'''

def tree(breach_len):
    if breach_len>5:
        t.forward(breach_len)
        t.right(20)
        tree(breach_len-15)
        t.left(40)
        tree(breach_len-15)
        t.right(20)
        t.backward(breach_len)

t = turtle.Turtle()
t.left(90) # 逆时针旋转90度
t.penup() # 提起笔移动，不绘制图形，用于另起一个地方绘制
t.backward(100)  # 向当前画笔相反方向移动distance像素长度
t.pendown() # 移动时绘制图形，缺省时也为绘制
t.pencolor('green') # 画笔颜色
t.pensize(2) # 画笔宽度

tree(75)
t.hideturtle()
turtle.done()

'''
turtle.forward(distance)    向当前画笔方向移动distance像素长度

turtle.backward(distance)   向当前画笔相反方向移动distance像素长度

turtle.right(degree)       顺时针移动degree°

turtle.left(degree)     逆时针移动degree°

turtle.penup()  提起笔移动，不绘制图形，用于另起一个地方绘制
turtle.pendown()    移动时绘制图形，缺省时也为绘制

turtle.goto(x,y)    将画笔移动到坐标为x,y的位置

'''
