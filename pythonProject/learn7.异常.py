#即debug
#捕获异常:
#try:
#     可能发生错误的代码
# except:

#捕获指定的异常
#try:
#    print(name)
# except （错误类型，如:NameError） as e(即异常的语句):
#     如果出现异常执行的代码
#多个
#except  (错误类型1，错误类型2...) as e:
#捕获全部:
#except Exception as e:

# else:(如果没有异常我该怎么做)
#finally:(不管有没有异常我都要去执行他,如最重要的关闭文件）