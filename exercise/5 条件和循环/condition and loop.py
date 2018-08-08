# 练习一 条件语句的使用
# 1
str1 = "0123456789"
if len(str1) == 10:
    print("字符串长度为10")
else:
    print("字符串长度不为10")

# 2
input_num = int(input('请输入一个1-40之间的整数：'))
if 1 <= input_num <= 10:
    print("数字在1-10之间")
elif 11 <= input_num <= 20:
    print("数字在11-20之间")
elif 21 <= input_num <= 30:
    print("数字在21-30之间")
else:
    print("数字在31-40之间")

# 练习二 循环语句的使用
# 1
for i in range(1,101):
    if i % 2 == 0:
        print (i)
# 2
j = 1 
while j <=100 :
    if j % 3 == 0:
        print(j)
    j += 1