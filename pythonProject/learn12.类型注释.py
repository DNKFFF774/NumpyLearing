#基础语法
#变量 : 类型  = 值
# import random
#
# var1:int = 10
# var2:list=[0,10,10,20]
# #可以对数据容器进行详细注解或者粗略注解
# mylist : tuple[int,str,float] = (19,"19",10.1)
# #方法2
# var3 = random.randint(1,10)# type:int

#函数类型注解
#def 函数方法名(形参名:类型,形参名:类型,形参名:类型...)->(返回值类型)：
def fuc(data:int)->int:
    print(f"function1,data={data}")
    return data+1
x=19
y=fuc(x)
print(y)
#Union类型进行注解
from typing import Union

def fuc2(data:Union[int,float])->Union[int,float]:
    print(f"function1,data={data}")
    return data+1

my_list:list[Union[str,int,float]] = [1,2,"byd",21.92]
