FAQ1:PYTHON支持的序列对象有哪些？
ANS1:字符串， 列表， 元组, 可以通过索引访问的对象

FAQ2:序列对象支持的操作符？
ANS2:
    1， 成员操作符，in、not in, 返回一个bool值
        in ：判断一个元素是在序列中
        not in ：判断一个元素不在序列中
    2， 连接操作符：+；如seq1 + seq2，生成一个新序列，包含seq1,seq2
    3， 重复操作符：*；如seq * n，生成一个重复n次seq的新序列
    4， 切片操作符：
        获取指定元素：seq[i1:i2]，获取序列索引为i1:i2-1的元素
        获取全部元素：seq, seq[:], seq[:None]
        获取翻转后的列表：seq[::-1]
        指定步进获取：seq[::step],表示以步进step进行获取

    说明：
        1, 切片反向取值，如seq[10:5]或者seq[-5:-10]，只能返回一个空列表
        2, 切片的开始和结束索引可以超过序列长度

FQA3:序列支持的内建函数？
ANS3:
    list(iter):把可迭代对象转换为列表；如list('abcd') -> ['a', 'b', 'c', 'd']
    str(obj):把对象转换为字符串
    tuple(iter):把可迭代对象转换为元组；如tuple('abcd') = ('a', 'b', 'c', 'd')
    enumerate(iter):返回一个enumerate对象，由key和value值组成的元组
        通常用于for循环，将元素与索引一一对应,如
        for i, v in enumerate('abcd'):
            print(i, v)
    len(seq):返回序列长度
    max(iter):返回序列最大值
    min(iter):返回序列最小值
    reversed(seq):返回一个逆序seq的reversed对象
    sorted(iter):返回一个排序后的iter对象
    sum(seq):返回序列的和
    zip(iter1, iter2)：将iter1，iter2压缩成一个列表，会自动排序

FAQ4:字符串大小比较
ANS4:字符串间的比较：字符串是按照ASCII值的大小来比较的.

FAQ5:格式化操作符
ANS5:
    %c:转换单一字符为ASCII码，与chr()功能相同
    %s:字符串格式化输出
    %d:十进制输出
    %o:八进制输出
    %x/%X:十六进制输出
    %f:浮点数输出
    %%:输出百分号
    格式化操作符辅助命令（可使用字符串的内建方法：str.center(width)，str.ljust(width), str.rjust(width), str.zfull(width)）:
        1， '%5d' % 9：输出占5位宽度，如
        In [48]: '%5d' % 9
        Out[48]: '    9'
        2， '%10.2f' % 1.2345：输出占10位宽度， 现在保留2位，如
        In [47]: '%10.2f' % 1.2364
        Out[47]: '      1.24'
        3， '%05d' % 1: 表示数字前补0，如：
        In [44]: '%05d' % 1
        Out[44]: '00010'
        4， 带格式输出十六进制，八进制
        In [49]: '%#x' % 15
        Out[49]: '0xf'

        In [50]: '%#X' % 15
        Out[50]: '0XF'

        In [51]: '%#o' % 15
        Out[51]: '0o17'
        5， 指定宽度，进行左对齐
        In [52]: '%-5d' % 5
        Out[52]: '5    '

FAQ6: 什么是原始字符串？
ANS6: 原始字符串中所以的字符都按字面意思来使用，不会出现转移, 使用方法为:r'str'

FAQ7: 字符串的内建方法？
ANS7:
检查字符串的开始和结尾：可以指定检查范围
str1.startswith('a', start, end)：检查是否以‘a’开始
str1.endswith('c', start, end)：检查是否以‘c’结束
其中start, end为指定的检查范围，为字符串索引
str1.isalnum():检查字符串是否仅由字母和数字组成
str1.isalpha():检查字串串是否仅由字母组成
str1.isdecimal():检查字符串是否只包含十进制数字组成
str1.isdigit():检查字符串是否只包含数字
str1.islower():检查str1是否全是小写字母
str1.isupper():检查str1是否全是大写字母
str1.isspace():检查str1是否仅由空格组成
str1.istitle():检查str1的所有单词，是否首字母都是大写
str1.capitalize():把字符串的第一个字符大写
str1.expandtabs(num):将字符串的制表符键转换为空格：返回转换后的字符串，num制表符替换成空格的数量
str1.replace(src, dest), 将src的内容用dest进行替换，可以指定替换次数
str1.swapcase():小写转换大写
str1.upper():所有字母转换为大写
str1.lower():所有字母转换为小写
str1.title()：将字符串的所有单词首字母大写
str1.count(sub， beg=0, end=len(string))：返回sub(子串)在字符串中出现的次数，可以指定查找范围
str1.find(sub, begin, end)：存在返回字串开始的索引值，否则返回 -1
str1.rfind(sub, begin, end)：从右边开始查找，返回元素的真实索引
str1.index(sub, begin, end)：功能和find一样，如果不存在抛出异常
str1.rindex(sub, begin, end)：从右边开始查找，功能和find一样，如果不存在抛出异常
str1.decode('utf8')：以utf8格式解码str1
str1.encode('utf8')：以utf8格式编码str1
连接符.join(seq)：以'连接符'连接seq中的每个字符，返回一个字符串
str1.split('分割符'):以'分割符'分割str1，返回一个列表， 默认分割服为空格，制表符，换行， 返回一个列表， 可指定分割的次数
str1.partition('分隔符'):以分隔符第一次出现的位子分割字符串为一个三元素的元组
str1.rpartition('分隔符')：从右边开始查找分割元素
str1.splitlines():按行进行分割，可指定切割行数
str1.center(width):字符串居中：width为指定的宽度,不足补空格
str1.ljust(width):字符串左对齐,不足补空格
str1.rjust(width)：字符串右对齐,不足补空格
str1.zfill(width)：右对齐，多余的补零
str1.lstrip()：截掉字符串左边的空格
str1.rstrip()：截掉字符串右边的空格
str1.strip()：截掉字符串两边的空格

FAQ8:列表的比较？
ANS8:列表：可变对象、列表间的比较是两个列表中的元素逐个比较，直到一方胜出

FAQ9：列表的内建函数
list1.extend(list2)：把序列list2的内容，添加到list1列表中
list1.count(obj)：查找元素， 返回obj在列表中出现的次数
list1.index(obj)：返回obj在list1中的第一个位置出现的索引，没有抛出异常
list.reverse()：反向输出列表
list.sort()：排序列表成员
list.insert(index, obj):指定下标插入元素
list.pop(index=-1):移除列表最后一个元素，也可以指定index进行元素移除
list.remove(obj):指定列表元素移除列表， obj存在多个时，移除一个查找到的

说明：列表所有的方法的结果都映射到列表本身，无返回值，除pop方法外（会返回移除的元素）

FAQ9:元组的访问以及内建方法
ANS9:
访问元组
tuple1：为一个元组

通过切片方式：
tuple1[start:end]

通过索引访问
tuple[index]

内建函数
obj在元组中出现的次数：
tuple1.count(obj):obj在元组中出现的次数
tuple1.index(obj):obj在元组中的索引值,没有抛出异常

常见问题：
1，列表运用extend方法，是没有返回值得，如下
a = [1]
b = a.extend([2])
输出结果：b为None

FAQ10:深拷贝与浅拷贝
ANS10:
浅拷贝：创建一个新对象，但是对象的值是员拷贝对象的引用；浅拷贝的方法：通过切片，工厂方法（list， tuple）
即使修改某个对象的值，影响到其他对象
如：
In [14]: persion = ['name',['saving', 100]]
In [14]: hubby = persion[:] #浅拷贝
In [14]: wifey = list(persion) #浅拷贝
In [27]: hubby[0]='joe'
In [28]: wifey[0]='jane'
In [30]: hubby[1][1]= 50.00 #修改某个值
In [31]: hubby, wifey
Out[31]: (['joe', ['saving', 50.0]], ['jane', ['saving', 50.0]]) #因为是浅拷贝，修该某个值，所有的值都被修改

深拷贝：创建一个新对象，对象的值也是新的；

