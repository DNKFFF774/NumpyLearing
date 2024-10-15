# 语法: def 函数名 (传入参数):
#             函数体
#             return 返回值
#注意函数说明手册格式

#如果函数没有写返回值，就会返回一个特殊的字面量：None,类型："NoneType"
#在if判断中，None等同于False，not None=Ture

#在函数内部修改全局变量:global+变量名

#实战演练：ATM
money=0
name=input("欢迎来到银行，请输入你的姓名：")
def check_money(flag):
    global money
    if not flag:
        print("\t----------------余额查询-------------\t")
    print(f"\t还剩下{money}元\t")
def save_money(num):
    print("\t----------------存款-------------\t")
    global money
    money+=num
    check_money(1)
    print("\t存款成功\t")
def take_money(num):
    print("\t----------------取款-------------\t")
    global money
    money-=num
    check_money(1)
    print("\t取款成功\t")
while True :
    print("\t----------------主菜单-------------\t")
    print("\t查询余额请按1\t")
    print("\t存款请按2\t")
    print("\t取款请按3\t")
    print("\t结束请按任意键\t")
    judge=int(input())
    if judge==1:
        check_money(0)
    elif judge==2:
        save_money(int(input("你要存款的数额是：")))
    elif judge==3:
        take_money(int(input("你要取款的数额是：")))
    else:
        break