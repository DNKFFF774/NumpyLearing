#元组和列表的不同：元组中的元素不可以被篡改，一旦定义完成，就不可以修改
#相当于只读的list
#元组用小括号定义
#from learn4_数据容器_列表 import mylist

tuple1=(1,"hello",True)
tuple2=()
tuple3=tuple()
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
t4=("hello",)#注意单个元素定义元组时的逗号
t5="hello"
print(f"t4的类型是{type(t4)}")
print(f"t5的类型是{type(t5)}")

#元组也支持下标索引
#操作1：查找index
print(tuple1.index(1))
#操作2：计数count
#操作3：len()计算元组之中的元素个数
#在元组之内定义一个list,这个list的数据是可以修改的
#--------------------------字符串---------------------------------------
#字符串的操作(也是不可修改的数据容器)
name=" itzhufeng and qinhuan "
a=name[0]
print(a)
#操作1：index，可以查找小字符串
print(name.index("and"))

#操作2：replace,将字符串替换,返回替换后的字符串
newstr=name.replace("and","or")
print(newstr)
print(name)
#操作3：分割split，得到一个列表对象,传入参数：按照哪个字符进行划分
Spl1=name.split(" ")
for index in Spl1:
    print(index)
print("分割",Spl1)
#操作4：规整操作strip() :去除前后空格
#       strip(字符串)去前后指定字符串(按照单个字符读取的)
#注意：本身还是不会改变
print(name)
newstr=name.strip()
print(newstr)
#操作5：统计字符出现字数:count
#操作6：统计字符串的长度:len()
#操作7：大小写操作：.title()可以把每个首字母大写,.upper()可以把全部大写；.lower()可以把全部小写
#——-----------------------------------------------------#
#序列：对前面三种类型的都可以进行的操作
#操作1：切片：不会影响序列本身，只会得到一个新的序列.语法：数据容器[起始位置：末位置：步长]
xulie=tuple1[1:3]
print(xulie)
print(type(xulie))
#生成的数据类型和原来的相同
#将字符串倒序[::-1]
#——-----------------------集合------------------------------#
#集合：不支持元素的重复{}
Kongjihe=set()#空集合
my_set={1,3,2,4,5}
print(my_set,type(my_set))
#集合不支持下标索引访问，但是允许修改
#
# 添加新元素
my_set.add("python")
my_set.add(0)
print(my_set)

#移除指定元素
my_set.remove("python")
print(my_set)

#随机取出来一个元素pop,因为不支持下标索引
print(my_set.pop())
print(my_set)

#清空 clear
# my_set.clear()
# print(my_set)

#取两个结果的差集
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
set4=set2.difference(set1)
print(set3)#1里面有2里面没有
print(set4)#2里面有1里面没有
#删除和两个集合中相同的部分
set1.difference_update(set2)
print(set1)
#两个集合合并
set3=set1.union(set2)
print(set3)
#联合本身并不会发生改变
#统计集合的元素数量len()

#集合的遍历
for i in set3:
    print(i)
#集合不能用while循环遍历，因为不支持下标索引
#---------------------------字典---------------------------------
#字典：通过key去检索value，如成绩单中通过姓名查找成绩
#定义也是{}但是存储的元素是键值对
#字典的key也不可以重复
dict_kong={}
dict1={"小王":100,"小李":80,"小陈":90}
#定义方式
print(dict1["小王"],type(dict1))
#key不可以为字典，其他的都可以
chengjidan={"王":{"语文":90,"数学":100,"英语":80}
,"陈":{"语文":96,"数学":90,"英语":77}
            }
print(chengjidan["王"]["语文"]) #可以通过两层key进行索引
#字典的常用操作:
# 新增:字典[key]=value（key原来不存在），若是存在，则为更新value值
#删除元素:pop:获得key对应的value，同时key被删除
ele=dict1.pop("小王")
print(f"{ele}{dict1}")
#清空元素clear
dict1.clear()
print(dict1)
#获得全部的key
mulu=chengjidan.keys()
mulu2=chengjidan["王"].keys()
print(mulu,type(mulu))
print(mulu2,type(mulu2))
#遍历字典
#方式1：
for i in mulu:
    for j in mulu2:
        print(chengjidan[i][j])
#方式2:
for i in chengjidan:
    print(i)
#统计字典内的元素数量
print(len(chengjidan))



#存储容器通用操作
# 1.max最大元素
# 2.min最小元素
# 3.通用转换：全部转换里列表，str，元组，集合等等
#list(转换对象) tuple(对象)str(对象)set(对象)
#4.通用排序功能 sorted(容器，reverse=true):排序结果通通变成列表