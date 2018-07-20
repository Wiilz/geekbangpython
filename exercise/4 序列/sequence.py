# 练习一 字符串

# 1
str1 = "Hello Python"
print(str1)

# 2
str2 = "Let's go"
print(str2)

# 3
str3 = " \"The Zen of Python\" -- by Tim Peters "
print(str3)

str3 = ' "The Zen of Python" -- by Tim Peters '
print(str3)

# 练习二 字符串的基本操作

# 1
string1 = 'xyz'
string2 = 'abc'
string3 = string1 + string2

# 2
print(string1[1]+string1[2])

# 3
for i in range(10):
    print(string2)

print(string2 * 10)

# 4
print('a' in string1)
print('a' in string2)

#练习三 列表的基本操作

# 1
list1= [1,2,3,4,5]
print(list1)

# 2
list1.append(100)
print(type(list1))
print(list1)

# 3
list1.remove(5)
print(list1)

#4
print(list1[0:3])
print(list1[-1])

#练习四
# 1

tuple1 = (1,2,3)
# tuple1.append(4)
# AttributeError: 'tuple' object has no attribute 'append'
# tuple1.append()

# 2
print(tuple1[-2])

# 3
tuple2 = (7,8,9,'a','b','c')
tuple3 = tuple1 + tuple2
print(len(tuple3))
print(tuple3.__len__())