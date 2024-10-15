#变量 Type 变量的类型
#盒子 变量名称=变量的值
money   = 40

print("钱包里还有",money)
print(type("傻逼"))

#注意type's outcome can be stored in 变量
#type 查看的是变量存储的数据类型，变量没有类型

print("---------------------------------")

#标识符  英文 下划线 数字  (数字不可以用在开头)
#运算符 **指数
a=5
b=2
print(a**b)
print(a//b)#整除，只需要整数部分
print(a%b)
print("---------------------------------")

#python 字符串的三种定义方法
name1="人间"
name2="有味"
name3="""是清欢"""
#转义字符\
name4="\'逐风\'"
print(name1)
print(name2)
print(name3)
print(name4)

print("---------------------------------")
#字符串拼接

print(name1+name2+name3)#字符串拼接
print(money+a)
#注意字符串不能和整数，浮点数这样的值进行拼接
#           |
#           |
#           |
#           |
#           |
#           进阶
#字符串格式化 通过占位的形式取拼接字符串
print("---------------------------------")
ShiJu="苏轼有言:%s%s%s" %(name1,name2,name3) #注意格式
print(ShiJu)
print("---------------------------------")
#%5d
print("价格为%3d" % money)
money2=11.3445
print("价格为%.2f" % money2)

print("---------------------------------")
#字符串格式化的快速写法 f"{变量}"
name1="人间"
name2="有味"
name3="""是清欢"""
print(f"苏轼有言：{name1}{name2}{name3}")
#特点：1.不在乎数据类型，2.也不进行精度控制 f format格式化的缩写
print(f"2+3={2+3}")
#特点：大括号里可以加入表达式



print("---------------------------------")


#数据输入input语句,使用一个变量去接收input从键盘读到的数据
name=input("你是谁")
age=input("你几岁")
print(f"你的名字是{name}，你的年龄是{age}")

#可知input语句只能输入str类型
int(age)#强制类型转换
print(name)
print(age)


