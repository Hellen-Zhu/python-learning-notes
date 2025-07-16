# ===========================================
# Python 列表修改
# ===========================================

print("=" * 50)
print("Python 列表修改")
print("=" * 50)

# ===========================================
# 1. 列表修改
# ===========================================
# 修改指定下标的元素
list1 = [1,2,3,4,5]
list1[2] = 10
print(list1)

# reverse() 反转列表 原列表改变
list2 = [1,2,3,4,5]
list2.reverse()
print(list2)

# sort() 排序 升序 原列表改变
list3 = [1,2,3,4,5]
list3.sort()
print(list3)

# sort() 排序 降序 原列表改变
list4 = [1,2,3,4,5]
list4.sort(reverse=True)
print(list4)

# 切片反转 得到新的列表，原列表不变
list4 = [1,2,3,4,5]
list4_new = list4[::-1]
print(list4_new)
print(list4)
