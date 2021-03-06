"""赋值运算符和变量"""

"""
一、 什么是赋值运算符以及什么是变量
    赋值运算符用=表示，=的左边是变量，=的右边是对象。
    在Python中，一切皆为对象
    变量相当于标签。对于赋值语句： 变量 = 对象，相当于给对象贴了一个标签，标签名就是变量名
    
    例如：
        对于赋值语句i = 18,
        Python会分配一块内存空间用于存储整数对象18，然后相当于给整数对象18贴上名为i的标签
        以后我们就可以通过名为i的标签访问整数对象18了
        接下来执行赋值语句 i = 23
        Python会再分配一块内存空间用于存储整数对象23
        然后相当于把名为i的标签从整数对象18撕下来并贴在整数对象23上，
        这样，我们就无法再通过名为i的标签访问整数对象18了
        
        接下来执行赋值语句 j = i
        相当于在整数对象23上又贴了一个名为j的标签，
        这样，我们即可以通过名为i的标签访问整数对象23， 又可以通过名为j的标签来访问整数对象23
    在某一时刻，一个标签只能贴在一个对象上，一个对象上可以贴多个标签
    变量是没有数据类型的，只有对象才有数据类型。
    
    通常情况下，一个变量只引用一种数据类型的对象。
"""

a = 18
print(a)  # 18

# 变量a引用了另外一种数据类型的对象（不推荐）
a = 'Hello'
print(a)  # Hello

"""
二、 赋值运算符支持链式赋值
    如果想让多个变量同时引用同一个对象，可以使用链式赋值。
"""

a = b = c = 18
print(a)  # 18
print(b)  # 18
print(c)  # 18

"""
三、赋值运算符支持参数赋值
    可以在赋值运算符的左边添加其它运算符，从而实现参数赋值，例如: +=、-=、*=、 /=、%=。
    a += b  相当于 a = a + b
    a -= b  相当于 a = a - b
    a *= b  相当于 a = a * b
    a /= b  相当于 a = a / b
    a //= b  相当于 a = a // b
    a %= b  相当于 a = a % b
    
    参数赋值可以代码更加简洁，而且可读性更强。
    
"""

a = 3
a += 5

print(a)  # 8

a -= 2
print(a)  # 6

a *= 8
print(a)  # 48

a /= 2
print(a)  # 24.0

a //= 5
print(a)  # 4.0

a %= 3  # 1.0
print(a)
