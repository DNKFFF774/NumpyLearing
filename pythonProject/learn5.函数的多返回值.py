# def test_return():
#     return 1,2
# x,y=test_return()
# print(x,type(x))
# print(y,type(y))
#函数传参：位置传参
#关键字参数:键=值
def testm (name,age,gender="中性"):#设置默认值必须在形参的最后面！！！！！！
    print(f"名字是{name}，年龄是{age}，性别是{gender}")

testm(name="关键字",age=12,gender="男")#顺序无所谓
#缺省参数：默认参数
testm(name="缺省",age=12)
#不定长传参
def user_info1 (*args):#默认元组，想传多少传多少
    print(args)
user_info1(1,2,3,4)
def user_info2 (**kwargs):#默认字典
    print(kwargs)
user_info2(name="Tom",age=18,id=110)#键=值的形式
#将函数传入另一个函数内

def test_func(countway):
    result=countway(2,3)
    print(result)
def compute(x,y):
    return x+y
def compute2(x,y):
    return x*y
#计算数据的逻辑是不确定的,但是计算的数据是确定的，太妙了，，妙不可言！！！
#完美的封装
#lambda匿名函数，无名称的函数，仅仅可以临时使用一次：只可以写一行代码
test_func(lambda x,y:x**y)#注意幂运算的写法，设定一个临时的运算逻辑
test_func(compute)
