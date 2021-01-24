"""读文件"""

"""
    读文件之前，必须先打开文件。
    可以调用内置函数open()并以只读方式或读写方式打开文件。返回的文件对象有三个用于读文件的方式:
1. read([size])
    如果不传参数,读到文件尾。
    如果传入参数，size用于指定字节数，
        当指定的字节数小于读到文件尾的字节数时，读取指定的字节数;
        当指定的字节数大于读到文件尾的字节数时，或当指定的字节数小于0，读到文件尾。
    如果文件较大，调用read()一次性读取整个文件导致内存占用较大，因此，最好多次调用read(size)。
    指定的size不要超过默认缓冲区的大小，否则，可能并不能读取到指定的字节数。通过标准库中模块io的
属性DEFAULT_BUFFER_SIZE可以查看默认缓冲区的大小:
    >>> import io
    >>> io.DEFAULT_BUFFER_SIZE
    8192
>>> file = open('myfile.txt')
>>> file.read()
'123'
>>> file.close()  # 文件在使用完毕后必须要关闭

>>> file = open('myfile.txt')
>>> file.read(12)
'123\nasdahaid'
>>> file.close()

>>> file = open('myfile.txt')
>>> file.read(12)
'123\nasdahaid'
>>> file.read(-5)
'shia\nadihdiahsdiahdi\nadhiahdia\n'
>>> file.close()
"""
"""
2.readline([size])
    如果不传递参数，读到行尾。
    如果传入参数，size用于指定字节数，
        当指定的字节数小于读到行尾的字节数时，读取指定的字节数;
        当指定的字节数大于读到行尾的字节数时，或当指定的字节数小于0，读到行尾。
    总之，最多读到行尾。
>>> file = open('myfile.txt')
>>> file.readline()
'123\n'
>>> file.readline(7)
'asdahai'
>>> file.readline(10)
'dshia\n'
>>> file.readline(3)
'adi'
>>> file.readline(-5)
'hdiahsdiahdi\n'
>>> file.close()
"""

"""
3. readlines([size])
    如果不传参数，读到文件尾，返回每一行组成的列表。
    如果传入参数，size用于指定字节数。
        当指定的字节数小于读到文件尾的字节数时，一直读取到最后一个字符所在行的行尾;
        当指定的字节数大于读到文件尾的字节数时，或当指定的字节数小于0，读到文件尾。
    如果文件较大，调用readlines()一次性读取整个文件导致内存占用较大，因此，最好多次调用readlines(size)。
指定的size不要超过默认缓冲区的大小，否则，可能并不能读取到指定的字节数。

>>> file = open('myfile.txt')
>>> file.readlines()
['123\n', 'asdahaidshia\n', 'adihdiahsdiahdi\n', 'adhiahdia\n']
>>> file.close()    
>>> file = open('myfile.txt')
>>> file.readlines(8)
['123\n', 'asdahaidshia\n']
>>> file.readlines(50)
['adihdiahsdiahdi\n', 'adhiahdia\n']
>>> file.close()
>>> file = open('myfile.txt')
>>> file.readlines(8)
['123\n', 'asdahaidshia\n']
>>> file.readlines(-5)
['adihdiahsdiahdi\n', 'adhiahdia\n']
>>> file.close()
"""


