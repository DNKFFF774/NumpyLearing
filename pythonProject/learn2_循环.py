#逻辑判断布尔类型和比较运算符
# result=10>5
# print(type(result))
# print(result)
# #6个比较运算符== != > < >= <=
print("---------------------------------")

#if语句
# age=int(input("请输入你的年龄"))
#
# if age>=18:
#     print("成年人,需要收门票钱")
# else:
#     print("小孩子免费")
# #集成
# if int(input("请输入你的年龄"))>=18:
#     print("成年人,需要收门票钱")
# else:
#     print("小孩子免费")

#python中是用空格缩进来判断归属的
#if 条件1 ：
#elif 条件2：
#elif 条件3：
#else :
#else :      多个条件判断格式
#随机数
import random
R_num=random.randint(1,10)
print(R_num)
#1-100的和
a=0
b=0
while a<=100:
    b=a+b
    a+=1
print(b)
#启示：判断值的改变总是应该放在最后面的

#99乘法表 while循环 2.for循环最优雅的写法
i=1
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}\t ",end='')
    print()
#for循环学习: 语法 for循环的机制是轮询，对一批内容进行逐个处理
#语法：for 临时变量 in 待处理数据集:（把数据集里面的数据赋给临时变量）
            # 处理
print("---------------------------------")
c=0
name="itheima is a brand of itcast"
for x in name:
    if x=='a':
        c+=1
print(c)
        #操作注意，必须是数据集，如字符串，列表，元组，等，更专业的叫法叫做“数列类型”
#第一个与C语言有着较大差别的语法， 无法定义无限循环

#range语句 作用：生成数字序列 其实就是数组
#1.range(num) 2.range(num1,num2) 3.range(num1,num2,step)
print("---------------------------------")
for x in range(1,2): # 快速锁定循环次数，较while来说更便捷
    print(f"今天是第{x+1}天")
print("---------------------------------")
#for循环规范：临时变量只是应该在for语句块里面使用。临时变量可以在for循环外部去定义，在之后就可以使用了

#break和continue的用法
money=10000
for x in range(1,21):
    score=random.randint(1,10)
    if money<1000:
        print("没钱啦，跑路吧")
        break
    elif score<5:
        print(f"第{x}名员工绩效是{score}不达标，没有工资")
        continue
    else:
        print(f"第{x}名员工绩效达标，领取工资{1000+score*100}元")
        money-=1000+score*100
print(f"剩余工资{money}元")
print("---------------------------------")
