print('hello world')
a=1
b=2
if a>b:#这行的作用是测试单行注释的编辑
    if a == 1:
        print(a)
    else:
        if a ==0:
            print(a)
        else:
            pass
elif a==b:
    print(a,b)
else:
    print(b)
'''
这段语句的作用是测试多行的注释编辑
'''
print('+');print('-')#用；分隔写在同一行的两条语句
if a>0:print('+')    #缩进的语句只有一条而写在同一行内
else:print('-')    #缩进的语句只有一条而写在同一行内
print('i am a teacher',\
      '++++',\
      '----')#“\”进行续航时，"\后不允许有任何内容
#Python中也规定了圆括号内包围部分是可以在不同行的
'''
name= input('please input your name:')#键盘输入
'''
print('a','b','c')
print('a','b','c',sep=',')     #将默认分隔符修改为','
print('a','b','c',end=';')     #将默认结束符号修改为';',则下一行输出与该句输出在同一行
print('a','b','c')
'''
*表示乘法，**表示幂运算
'''
import math
x=2
e=math.sin(x)#使用sin函数时，要先调用math库
print(e)