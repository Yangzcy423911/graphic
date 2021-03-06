"""循环结构的概述"""
"""
一、 为什么需要循环结构
    如果要打印1到10之间的所有自然数，你可能会这样实现：
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
    如果要打印1到1000之间的所有自然数，你就要写1000行代码，而且这1000行代码都是重复的
print语句，唯一的区别在于要打印的自然数不同。
二、什么是循环结构
    使用循环结构，上面的需求可以这样实现:
i = 1
while i < 11:
    print(i)
    i += 1
或者这样实现:
for i in range(1, 11):
    print(i)
代码量少了很多，而且没有重复的代码。
如果要打印1到1000之间的所有自然数，只需要把11改为1001就可以了。

    循环结构指的是： 程序根据循环条件反复执行某段代码，直到不满足循环条件为止。
    
    Python提供了两种实现循环结构的语句： while语句和for-in 语句
"""