#模块导入操作[from 模块名] import [模块|类|变量|函数|*][as 别名]
# import time
# time.sleep(6)
from time import  sleep
sleep(3)

#if __name__ == '__main__':
#此语句用来自定义模块时测试代码输出使用
# __all__ = ['函数名称'] 此语句用来与import *搭配引用
# 导入包：import 包名.模块名
# 包名.模块名.功能

#或 from 包名 import 模块
#模块.功能

#或 from 包名.模块 import 功能
#功能

#注意当名字冲突时可以用as（alias）来别名使用函数,模块也可以使用别名