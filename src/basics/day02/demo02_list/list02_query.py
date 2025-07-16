# ===========================================
# Python 列表查询
# ===========================================

print("=" * 50)
print("Python 列表查询")
print("=" * 50)

# ===========================================
# 1. 列表查询
# 列表中没有find方法，只有index方法
# ===========================================

# index() 找到返回下标，找不到报错 ValueError
list1 = [1,2,3,4,5]
print(list1.index(3))

# count()
list2 = [1,2,3,4,5,3]
print(list2.count(3))

# count() 找到返回出现的次数，找不到返回0
list3 = [1,2,3,4,5,3]
print(list3.count(3))

# in 找到返回True，找不到返回False
list4 = [1,2,3,4,5]
print(3 in list4)

# not in 找到返回False，找不到返回True
list5 = [1,2,3,4,5]
print(3 not in list5)

