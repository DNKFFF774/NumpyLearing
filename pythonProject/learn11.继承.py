#继承
class Phone:#父类
    IMEI=None
    producer= "apple"
    # def __init__(self,IMEI,P):
    #     self.IMEI=IMEI
    #     self.producer=P
    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):#子类(单继承),多继承就是多加几个逗号就可以
    face_id=True
    def call_by_5g(self):
        print("2022最新5G通话")

class Phone2024(Phone2022,Phone):# 继承的顺序：谁先来，谁的优先级最高，即同名时的情况
    pass#用于集成父类，没有新增功能的子类通过编译

#复写：子类中复写父类属性或者父类方法
class Phone2077(Phone2022,Phone):# 继承的顺序：谁先来，谁的优先级最高，即同名时的情况
    producer = "2077w"
    def call_by_5g(self):
        # print("2077最新5G通话")
        #方式1
        # print(f"父类的厂商名是{Phone.producer}")
        # Phone2022.call_by_5g(self)
        # print("省电模式开启")
        # print("确保性能")
        #房市2
        print(f"父类的厂商名是{super().producer}")
        super().call_by_5g()
        print("省电模式开启")
        print("确保性能")


phone=Phone2077()
phone.call_by_5g()
#子类中调用父类成员
#调用成员变量：父类名.成员变量
#调用成员方法：父类名.成员方法(self)
#
#2:
#super()成员变量
#super().成员方法()
#
#
