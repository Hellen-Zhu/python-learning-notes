# ===========================================
# Python 列表详解
# ===========================================

print("=" * 50)
print("Python 列表详解")
print("=" * 50)

# ===========================================
# 1. 列表的定义和创建
# ===========================================
# 使用类实例化的方式
list1 = list()
print(list1)

list2= list('abc')
print(list2)


# 直接使用[]进行定义
list3 = []
print(list3)

list5=[1,'abc',True]
print(list5)

#获取第一个元素
print(list5[0])

#获取最后一个元素
print(list5[-1])

#获取倒数第二个元素
print(list5[-2])

# 使用range()函数创建列表
list4 = list(range(10))
print(list4)

print(list4[0:3])
print(list4[0:3:2])