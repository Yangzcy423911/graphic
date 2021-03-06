"""模块内的数据访问控制之特殊属性__all__"""

"""
    为了在某种程序上实现模块内的数据访问控制，还可以在模块内定义特殊属性__all__。这样，
使用语句"from 模块名 import *"只能导入特殊属性__all__中定义的属性，但是，
使用语句"import 模块名"仍然可以导入所有的属性。
"""


"""
    当使用语句"from 模块名 import *" 导入属性时，
如果既在模块内的某个属性前添加了单下划线_,又将这个属性定义在模块内的特殊属性__all__中，
那么__all__比单下划线具有更高的优先级。
"""
