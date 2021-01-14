"""类对象的特殊方法之__del__()"""

"""
    系统会自动销毁不在需要的对象以释放内存。因此，当对象被销毁时通常不需要手动地执行清理工作。
但是，当使用我们自己创建的资源时，可能需要执行一些额外的清理工作，例如，如果创建了一个自定义的
类对象来打开一个文件并写入一些数据，可以需要在实例对象被销毁之前关闭该文件。为了执行这些额外的
清理工作，可以在自定义的类对象中实现特殊方法__del__()。
    当内存中的对象被销毁（垃圾回收）之前，会自动地调用其对应的特殊方法__del__()。
    当对象的引用计数为0时，对象并不会立刻被销毁（垃圾回收），何时进行垃圾回收是不确定的。因此
特殊方法__del__()何时会被调用也是不确定的。
"""


class MyClass(object):
    def __del__(self):
        print("特殊方法__del__被调用")


mc = MyClass()

del mc
