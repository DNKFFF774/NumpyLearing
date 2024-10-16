#对数据的组织
#类

# class Student:
#     name = None
#     gender = None
#     nationality = None
#     age = None
# #这些都是"成员变量"
#     def age_print(self):
#         print(f"my age is {self.age}")#self表示成员方法
# # 类的行为:即类之中的函数
#     def __init__(self,name,gender,na,age):
#         self.name=name
#         self.gender=gender
#         self.age=age
#         self.nationality=na
# #写了init,前面成员变量的声明可以不用写了（构造方法）
#
# stu_1=Student(1,1,1,1)
# stu_1.age=18
# stu_1.age_print()
# #构造方法__init__: 在创建对象（构造类的时候会自动执行的行为）
# stu_2=Student("JACK","boy","CN",20)
# print(stu_2.name)


#魔术方法 ：构造方法，字符串方法，符号比较方法

# class Student:
#     name = None
#     age = None
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"Student类对象,name={self.name},age={self.age}"
#     def __lt__(self, other):
#             return self.age<other.age
#     def __le__(self,other):
#             return self.age<=other.age
#     def __eq__(self, other):
#             return self.age == other.age
# #写了init,前面成员变量的声明可以不用写了（构造方法）
# stu_1=Student("wang",20)
# stu_2=Student("chen",30)
# print(str(stu_1))
# print(stu_2<stu_1)
# print(stu_2<=stu_1)
# print(stu_2==stu_1)


#m面向对象三大特性:封装 继承 多态
#私有成员变量和私有成员方法

# class Phone:
#     __current_voltage=20 #私有变量无法直接使用，不能读也不能写,但是类中的成员可以读取
#
#     def __keep_single_core(self):
#         print("CPU single core mode")
#
#     def ModeChosen(self):
#         if self.__current_voltage>10:
#             self.__keep_single_core()
#         else:
#             print("error")
#
# phone1=Phone()
# phone1.ModeChosen()

#练习

# class Phone:
#     __is_5g_enable=False
#     __name=None
#
#     def __check_5g(self):
#         if self.__is_5g_enable==True:
#             print("5g开启")
#         else:
#             print("5g关闭,使用4g网络")
#     def call_by_5g(self):
#         self.__check_5g()
#         print("正在通话中")
# phone_1=Phone()
# phone_1.call_by_5g()



