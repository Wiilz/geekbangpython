# 1. 在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
# 使用未定义变量
# a + 1
# NameError: name 'a' is not defined

# 访问列表不存在的索引

# b = [1,2,3]
# print(b[3])

# IndexError: list index out of range

# 访问字典不存在的key

# c = {'x':1}
# print (c['y'])

# KeyError: 'y'

# 2. 通过Python程序产生IndexError，并用try捕获异常处理

try:
    b = [1, 2, 3]
    b[3]
except IndexError:
# except Exception as e:
#   print(e)
    print(u'访问列表不存在的索引')
