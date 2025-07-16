# ===========================================
# Python 字符串常用方法详解
# ===========================================

print("=" * 50)
print("Python 字符串常用方法详解")
print("=" * 50)

# ===========================================
# 1. 字符串split方法
# 默认按照空白字符进行分割
# 语法:str.split(sep=None, maxsplit=-1)
# 参数:
# sep:分割符，默认为None，即按照空白字符进行分割
# 空白字符:空格、\t、\n、\r
# maxsplit:分割次数，默认为-1，即分割所有
# 返回值:
# 分割后的列表
# 示例:
my_str = "hello world\t and python\n and java"
print(my_str.split())
print(my_str.split(" "))
print(my_str.split("\t"))
print(my_str.split("\t",))
print(my_str.split("\n"))
print(my_str.split("\n"))

my_str = "hello world and python and java"
print(my_str.split('and'))