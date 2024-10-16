# 数据容器可以分为5类有：列表、元组、字符串、集合、字典
name_list=["小张","小李","小王"]
list_1=[666,True,"这是一个字符串",name_list]
print(name_list)
print(list_1)
#list 中可以存储不同数据类型的数据,而且列表支持嵌套
print(type(name_list))
#list一种数据类型
print("---------------------------------")
#从列表中取出元素
for i in range(1,5):
    print(-i,list_1[-i])
print(list_1[3][1])

#支持倒着检索，倒数第一个是-1 倒数第二个是-2以此类推

print("--------------查找-------------------")
#列表的常用操作：方法class，将函数定义为class的成员，函数就会被称为方法
#而class就是类对象
#方法1：查找某一元素的下标 列表.index（元素）
# 还有语法in 和 not in ，输出分别为True和False
print (name_list.index("小王"))
print (list_1.index(666))
#方法2；修改特定下标索引的函数 列表[下标]=值
#方法3：在指定的下标位置插入指定的元素；列表.insert（下标，元素）
print("--------------插入-------------------")
mylist=[1,2,4]
mylist.insert(2,3)
print(mylist)
print("--------------追加-------------------")
#方法4：追加元素，在列表的尾部
mylist.append(5)
print(mylist)
#追加一批元素，语法：列表.extend(其他数据容器)
mylist.extend(name_list)
print(mylist)
#方法5：元素删除:语法1：del 列表[下标]
#      可以取出 语法2：列表.pop(下标)
print("--------------删除-------------------")
del mylist[5]
print(mylist)
element=mylist.pop(5)
print(mylist,f"取出的元素是{element}")
#方法6：删除哪一个元素 list.remove(具体的元素)（只能删掉最前面的一个）
mylist.remove("小王")
print(mylist)
#方法7：清空列表 语法：list.clear()
mylist.clear()
print(mylist)#输出空列表
print("--------------统计-------------------")
#方法8:统计某个元素在列表中的数量
mylist.extend([1,1,2,3,4,4,4,5])
print(mylist.count(4))
#方法9:计算列表元素数量
print(len(mylist))
print(len(list_1))
#方法9:对列表中的元素进行不可逆排列：sort（），可逆排列sorted（），反向在里面加reverse=True
print("--------------遍历-------------------")
#for 临时变量 in 数据容器(list):
#    对临时变量进行处理
#    也可也使用range，range(1,5)里面通常是1，2，3，4并不包含5
#     还有列表推导式的逻辑理解