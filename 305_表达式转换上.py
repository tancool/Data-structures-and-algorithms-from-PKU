
'''
中坠表达式  前缀表达式  后缀表达式
(从左到右)  (从右到左)
a+b       +ab       ab+

a+b*c     +a*bc     abc*+

a+b*c     +a*bc     abc*+

a+b*c+d   ++a*bcd   abc*+d+

(a+b)*(c+d) *+ab+cd ab+cd+*

a*b+c*d   +*ab*cd   ab*cd*+

a+b+c+d    ++++abcd  ab+c+d+
'''