#open打开函数：打开文件或者创建新文件open(name,mode,encoding)
#mode:r:只读;w 从头开始编辑，原先内容会被删除;a:追加，在原有内容之后进行追加
# f = open("C:/Users/WyofarMoon/Desktop/python操作.txt","r",encoding="UTF-8")
#操作方法
#.read(num),表示从文本中读取数据的长度，单位是字节，无num就是所有
#.readline()按照行的方式进行全部读取，并且返回一个列表，每一行数据是一个元素
# print(f.read(8))

# listp=f.readlines()
# print(listp)

#循环

# for line in f:
#     print(line,end='')
# f.close()
#with open语法： 自动帮助关闭打开的文件，防止忘记close
#with open(,,,) as 名称:
    # 操作
# with open("C:/Users/WyofarMoon/Desktop/python操作.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         print(line,end='')


#------------------写入------------------------------
f = open("C:/Users/WyofarMoon/Desktop/python操作.txt","r",encoding="UTF-8")
f2 = open("C:/Users/WyofarMoon/Desktop/python操作2.txt","w",encoding="UTF-8")

# 文件写入:f.write(内容)
#刷新:f.flush()
list1=f.readlines()
for jk in list1:
    f2.write(jk)
    
f.close()
f2.close()