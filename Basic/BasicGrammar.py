# -*- coding: utf-8 -*-
# 定义允许在源文件中使用 utf-8 字符集中的字符编码


"""
import 与 from...import

在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
"""
# 导入 sys 模块
import sys
print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('python 路径为', sys.path)

from sys import argv, path  # 导入特定的成员
print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path


# 导入keyword包并将keywordList打印出来
import keyword

print("保留字")
print(keyword.kwlist)


'''
标识符
第一个字符必须是字母表中字母或下划线 _ 。
标识符的其他的部分由字母、数字和下划线组成。
标识符对大小写敏感。
在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了
'''
# 单行注释
print("行后注释")  # 行后注释
# 多行注释1
# 多行注释2
'''
多行注释3
'''
"""
多行注释4
"""


'''
行与缩进
python最具特色的就是使用缩进来表示代码块，不需要使用大括号{}
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
程序由于缩进不一致，执行后会出现类似以下错误：
IndentationError: unindent does not match any outer indentation level
'''


'''
多行语句
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
'''
one = 1
two = 2
three = 3
four = 4
five = 5
total1 = one + \
         two + \
         three
print(total1)
'''
在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
'''
total2 = ['one', 'two', 'three',
          'four', 'five']
print(total2)


# 输出空行
print('\n')
# 输出 \n
print(r'\n')
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
# 不换行输出
print("不换行输出，", end="")
# 换行输出
print("换行输出")


# 从控制台获取用户输入
anyhow = input("随便输入点什么吧")
print(anyhow)


'''
同一行显示多条语句
Python 可以在同一行中使用多条语句，语句之间使用分号;分割
'''
x = '同一行显示多条语句';
sys.stdout.write(x)
