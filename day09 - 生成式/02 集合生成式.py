"""集合生成式"""

"""
一、 什么是集合生成式
    如果想要生成集合{1, 4, 9, 16, 25, 36},可以使用for-in循环:

"""
s = set()
for i in range(1, 7):
    s.add(i * i)
print(s)  # {1, 4, 36, 9, 16, 25}
"""
    上述的解决方案有更好的替代，那就是使用集合生成式。
    集合生成式的语法:[表示集合元素的表达式 for 自定义的变量 in 可迭代对象].
其中，"表示集合元素的表达式"中通常包含"自定义的变量"。
    集合生成式的使用场景: 凡是可以通过for-in循环创建的集合，都可以使用集合生成式来创建。
"""
s = {i * i for i in range(1, 7)}
print(s)  # {1, 4, 36, 9, 16, 25}

"""
二、在集合生成式中使用if语句
    可以在集合生成式的for-in循环后添加if语句。
"""
s = {i * i for i in range(1, 7) if not i % 2}
print(s)  # {16, 4, 36}

# 以上代码相当于:
s = set()
for i in range(1, 7):
    if not i % 2:
        s.add(i * i)
print(s)  # {16, 4, 36}

"""
三、 在集合生成式中使用双重循环
"""
s = {(i, j) for i in range(1, 4) for j in range(1, 4)}
# {(1, 2), (2, 1), (3, 1), (1, 1), (2, 3), (3, 3), (2, 2), (3, 2), (1, 3)}
print(s)

# 以上代码相当于:
s = set()
for i in range(1, 4):
    for j in range(1, 4):
        s.add((i, j))
# {(1, 2), (2, 1), (3, 1), (1, 1), (2, 3), (3, 3), (2, 2), (3, 2), (1, 3)}
print(s)

# 既使用双重for-in循环，又使用if语句
s = {(i, j) for i in range(1, 4) for j in range(1, 4) if i != j}
print(s)  # {(1, 2), (2, 1), (3, 1), (2, 3), (3, 2), (1, 3)}
