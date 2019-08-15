'''
使用匿名函数
'''
import cmath
s = lamda x1,x2,y1,y2:cmath.sqrt((x1-x2)**2+(y1-y2)**2)
print(s(1,2,3,4))