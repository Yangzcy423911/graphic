""" 函数的定义和调用"""
"""
一、定义函数
    定义函数的语法格式:
def 函数名([形式参数1, 形式参数2, ...., 形式参数n]):
    函数体
其中，def是Python定义的关键字。
    关于函数名的说明:
  (1) 每个函数都有一个函数名，用于函数的调用。
  (2) 函数名属于标识符，因此，必须遵守标识符的命名规则，推荐遵守标识符的命名规范。此外，函数名
 最好是动宾格式，以表明函数完成的特定功能，例如: handle_message、print_result。
    关于形式参数的说明:
  (1) 形式参数简称形参。
  (2) 形参用于在调用函数时接收输入，也就是接收传递的实际参数（简称实参）。
  (3) 形参用中括号起来，表示形参时可选的，也就是说，可以定义也可以不定义。
  (4) 形参的本质是变量，其作用域(起作用的范围)仅限于函数体。
    关于函数体的说明:
  (1) 函数体是用于执行特定任务以完成特定功能的主体代码。
  (2) 函数体对应的代码块必须缩进。
  (3) 如果函数需要有输出(返回值)，可以在函数体内通过语句return xxx 进行返回，同时结束函数体的
 执行。如果函数不需要有输出（返回值），可以在函数体内通过语句return直接结束函数体的执行，或者让函数体
 正常执行结束，其实，函数在这两种情况下都是有返回值的，其返回值都是None
 （4）函数体在调用函数时才会被执行，因此，定义函数不会改变程序的执行流程。
"""


def decide_args(arg1, arg2):
    if arg1 and arg2:
        return arg1, arg2
    elif (not arg1) and (not arg2):
        return
    else:
        result = arg1 or arg2


"""
    定义函数后，就创建了一个函数对象，它的类型是function.
"""
print(decide_args)  # <function decide_args at 0x10ce9c670>
print(type(decide_args))  # <class 'function'>

"""
二、调用函数
     调用函数时，每个实参都被用于初始化相应的形参。所有形参都被初始化之后，函数体对应的代码块
被执行。程序的执行流会跳转到定义函数的函数体内，执行函数体对应的代码块，执行完函数体后再跳回到
调用函数的地方，继续执行下一条语句。
"""

print(decide_args(18, 'Hello'))  # (18, 'Hello')

print(decide_args([], {}))  # None

print(decide_args(18, []))  # None