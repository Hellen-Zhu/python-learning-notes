# ===========================================
# Python 元组定义
# ===========================================

print("=" * 50)
print("Python 元组定义")
print("=" * 50)

# ===========================================
# 1. 元组定义
# ===========================================
# 使用类实例化的方式
# 直接使用()进行定义
# 使用tuple()函数进行定义
tuple1 = tuple() # 空元组,不推荐，元素创建后不可更改
print(tuple1)

tuple2 = tuple('abc')
print(tuple2)

tuple3=tuple([1,2,3])
print(tuple3)

# 使用range()函数进行定义
tuple4 = tuple(range(10))
print(tuple4)

# 使用list()函数进行定义
tuple5 = tuple(list(range(10)))
print(tuple5)

# 使用dict()函数进行定义
tuple6 = tuple(dict(name='张三',age=18))
print(tuple6)

# 使用set()函数进行定义
tuple7 = tuple(set([1,2,3,4,5]))
print(tuple7)

# 使用frozenset()函数进行定义
tuple8 = tuple(frozenset([1,2,3,4,5]))
print(tuple8)

tuple9 = 1,2,3
print(tuple9)

# 解包，将元组中的元素赋值给多个变量
a,b,c = tuple9
print(a,b,c)

a=10
b=20
c= a,b
print(c)

a,b=b,a
print(a,b)

# 元组中只有一个元素时，需要在元素后面加一个逗号，否则会被认为是整数
d=(1,)
print(d)

# 元组中只有一个元素时，需要在元素后面加一个逗号
e=(1)
print(e)