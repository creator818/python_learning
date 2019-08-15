#实现列表推导
square=[i**i for i in range(1,11)]
print(square)
#不适用列表推导，使用for循环
square=[]
for i in range(1,11):
    square.append(i**i)
print(square)
'''
字典的推导语句
'''
keys=['name','age','weight']
values=['bob','22','75']
adct={k:v for k,v in zip(keys,values)}
print(adct)
'''
推导进阶
还可以使用if语句
'''
square=[i**i for i in range(1,11) if i**i %2 == 1]#实现有选择的处理序列中的元素
print(square)
def hello():
    print('你好啊')
hello()
def sum_tpl(T):
    result=0
    for i in T:
        result += i
    return result
print('[1,2,3]列表中元素之和为：',sum_tpl([1,2,3]))
print('(1,2,3)元组中元素之和为：',sum_tpl((1,2,3)))#说明不同类型的参数可以调用同一个函数
''''
深入函数
针对的是是否传递参数
还有就是参数数量不确定
'''
#默认值参数,多参数时，首先声明无默认值参数，后
def hello(name='1+'):
    print('你好，%s'%name)
hello()
hello('+++1')
def hello(name='1+',word='cc'):
    print('%s love %s'%(name,word))
hello(word='gc')
def mult(a=1,b=2,c=3):
    return a+2*b+c*3
print(mult(9,c=5,b=6))#按顺序传递的参数要位于关键字参数之前，并且不能重复
#无默认值参数优先放在前面，有默认参数的放后面,出现可变长参数时放最后面，**可以用来收集多余参数（k=3）

def change_para(*tp1):
    print(type(tp1),tp1)

change_para(1)
change_para(1,2,3)

def cube(name,**nature):
    all_nature={
        'x':1,
        'y':2,
        'z':3,
        'color':'white',
        'weight':'heavy'
    }
    all_nature.update(nature)
    print(name,'立方体属性')
    print('体积',all_nature['x']*all_nature['y']*all_nature['z'])
    print('color',all_nature['color'])
    print('heavy',all_nature['weight'])

cube('first')
cube('second',y=6,color='red')
cube('third',z=8,color='green',weight='10')

def mysum(a,b):
    return a+b

print('拆解元组调用',mysum(*(3,4)))#元组作为位置参数
print('拆解字典调用',mysum(**{'a':3,'b':5}))#拆解字典作为关键字参数

def change(aint,alist):
    aint=0
    alist[0]=0
    alist.append(4)
    print(aint)
    print(alist)

aint=3
alist=[1,2,3]
print(aint)
print(alist)
change(aint,alist)
print(aint)#调用后整数参数不发生变化
print(alist)#调用后列表发生变化

def myfun(lst=[]):
    lst.append('abc')
    print(lst)

myfun()
myfun()
myfun()

def myfun():
    a = 0
    a += 3
    print('a的值是：',a)

a = 'external'

print()

def myfun():
    global a#使用全局变量
    a = 0
    a += 3
    print("function 内的a",a)

a = 'external'

print('全局作用域:',a)
myfun()
print('全局作用域:',a)
