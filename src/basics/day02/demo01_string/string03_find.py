# ===========================================
# Python 字符串详解
# ===========================================

print("=" * 50)
print("Python 字符串常用方法详解")
print("=" * 50)

# ===========================================
# 1. 字符串find方法
# ===========================================
print("\n1. 字符串find方法")
print("-" * 40)

# 1.1 字符串find方法
# find方法用于在字符串中查找子字符串，如果找到则返回子字符串的索引，否则返回-1
# 语法：str.find(sub[, start[, end]])
# 参数：
# sub：要查找的子字符串
# start：开始查找的索引位置，默认为0
# end：结束查找的索引位置，默认为len(str)
# 返回值：
# 如果找到子字符串，则返回子字符串的索引，否则返回-1
# 示例：
my_str = "hello world"
print(my_str.find("world"))
print(my_str.find("python"))
print(my_str.find("world", 0, 5))
print(my_str.find("world", 6, 11))
print(my_str.find("world", 6, 10))
print(my_str.find("world", 6, 12))
print(my_str.find("world", 6, 13))
print(my_str.find("world", 6, 14))