'''
今天学习循环语句
'''
x=input('Please input a integer:')
x=int(x)
#if语句注意特点是条件之后有“：”
if x<0:
    print('你输入了一个负数')
else:
    print('你输入了一个非负数')
'''
如果是需要多重条件判断的话，需要使用elif
当满足第一个elif时，程序会跳出循环，只输出第一个满足条件的语句
'''
if x<0:
    print('你输入了一个负数')
elif x==0:
    print('你输入了一个0')
else:
    print('你输入了一个非负数')
'''
if也可以用于单语句中，实现三元运算符
下面语句实现的是如果a不为None,则x=b,否则x的值取0
'''
'''
a=None
b = 3
x = b if a is not None else 0
print(x)
'''

'''
if可以嵌套使用，其区别就是缩进量不同，要保证缩进量
'''
if x>0:
    if x>10:
        print('无法表示')
    else:
        print("可以表示")
else:
    print('输入的是负数')

'''
for 语句，break语句，continue语句
'''
for i in [1,2,3,4,5]:#i是循环变量，每次循环，i依次取后面列表的值
    print(i,'的平方是：',i*i)#这是循环体
else:#for循环结束之后执行的语句
    print('循环结束！')
'''
break的语句作用是终止for的遍历,执行完本轮循环
continue的作用是提前停止本轮循环，进入下一个遍历循环
for 如果不是正常结束，则else中的语句不会执行
else可以不被执行
'''
for i in [1,2,3,4,5]:#i是循环变量，每次循环，i依次取后面列表的值
    print(i)
    if i == 2:
        continue
    print(i,'的平方是：',i*i)#这是循环体
    if i == 4:
        break
else:#for循环结束之后执行的语句
    print('循环结束！')
'''
for用于执行字典的遍历
'''
adct = {'apple':15,'banana':20,'pear':12}
for key,value in adct.items():
    print(key,':',value)
for key in adct.keys():
    print(key)
for value in adct.values():
    print(value)
'''
range用于产生一个整数列表，用于完成计数循环
start默认是0
'''
print('第一次循环输出')
for i in range(4):
    print(i)
print('第二次循环输出')
for i in range(0,7,2):
    print(i)
'''
for 也可以嵌套使用
查找任意两个数之间的素数例子
'''
shuru=(int(input('输入一个值')),int(input('输入结束值')))
x1=min(shuru)
x2=max(shuru)
for n in range(x1,x2+1):
    for i in range(2,n-1):
        if n%i == 0:
            break
    else:
        print(n,'是素数')
'''
for语句与内置迭代函数
enumerate(seq)编号迭代
sorted(seq)排序迭代
reversed(seq)翻转迭代
'''
for i , item in enumerate('adcd'):#既输出元素序号又输出元素值
    print('第%d个字符是：%s'%(i,item))
#排序迭代的特点是先遍历序列中较小的值，后遍历较大的值
for i in sorted([3,1,6,5]):
    print(i)
#翻转迭代的特点是将元素从尾至头遍历
for i in reversed([3,1,6,5]):
    print(i)
#并行迭代也是一种经常使用的方法
lsta=(1,2)
lstb=(2,3)
lstc=(3,5)
for i,j,k in zip(lsta,lstb,lstc):
    print('%d+%d=%d'%(i,j,k))

'''
while 循环执行语句
while语句只有在测试语句为假时，才停止迭代
'''
alst=[1,2,3,4,5]
total= len(alst)
i = 0
while i < total :
    print(i+1,'的平方是',alst[i]*alst[i])
    i+=1#字符串和整数不能相加
else:
    print('循环结束')
square = [i**i for i in range(1,11)]
print(square)
