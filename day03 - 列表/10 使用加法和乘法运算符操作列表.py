"""使用加法和乘法运算符操作列表"""

"""
一、 如何使用加法运算符操作列表
       可以使用加法运算符将两个列表合并后生成一个新列表，被合并的两个列表不发生任何变化
"""

L1 = [1, 2, 3]
L2 = [4, 5, 6]

L3 = L1 + L2
print(L3)  # [1, 2, 3, 4, 5, 6]
print(L1)  # [1, 2, 3]
print(L2)  # [4, 5, 6]
"""
    参数赋值运算符+=会对列表本身进行修改
"""
L1 = L2 = [1, 2]
L1 = L1 + [3, 4]
print(L1, L2)   # [1, 2, 3, 4] [1, 2]

L1 = L2 = [1, 2]
L1 += [3, 4]
print(L1, L2)  # [1, 2, 3, 4] [1, 2, 3, 4]

"""
二、 使用乘法运算符操作列表
     可以使用乘法运算符将列表中的所有元素重复n次后生成一个新列表，被乘的列表不发生任何变化。
"""
L1 = [1, 2, 3]
L = L1 * 3
print(L)   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(L1)  # [1, 2, 3]
# 常用于列表的初始化
L = [0] * 5
print(L)   # [0, 0, 0, 0, 0]

"""
    参数赋值运算符*=会对列表本身进行修改
"""
L1 = L2 = [1, 2]
L1 = L1 * 3
print(L1, L2)   # [1, 2, 1, 2, 1, 2] [1, 2]

L1 = L2 = [1, 2]
L1 *= 3
print(L1, L2)    # [1, 2, 1, 2, 1, 2] [1, 2, 1, 2, 1, 2]