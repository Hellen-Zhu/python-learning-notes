# ===========================================
# Python 列表更新
# ===========================================

print("=" * 50)
print("Python 列表更新")
print("=" * 50)

# ===========================================
# 1. 列表更新
# ===========================================
# append() 追加元素
list1 = [1,2,3,4,5]
list1.append(6)
print(list1)

# extend() 追加列表
list2 = [1,2,3,4,5]
list2.extend([6,7,8,9,10])
print(list2)

# pop() 删除指定下标的元素,默认删除最后一个元素
list3 = [1,2,3,4,5]
list3.pop()
print(list3)

# pop() 删除指定下标的元素
list4 = [1,2,3,4,5]
list4.pop(2)
print(list4)

# remove() 删除指定元素
list5 = [1,2,3,4,5]
list5.remove(3)
print(list5)

# clear() 清空列表
list6 = [1,2,3,4,5]
list6.clear()
print(list6)