# 练习
# 1. 定义一个列表，包含10个元素，元素为1-10的随机数
# 2. 打印列表中最大的元素
# 3. 打印列表中最小的元素
# 4. 打印列表中所有元素的和
# 5. 打印列表中所有元素的平均值

list0 = list(range(1,11))
print(list0)

print(max(list0))
print(min(list0))

num=0
for i in list0:
    num +=i
    i+=1
print(num)
print(num/ len(list0))
