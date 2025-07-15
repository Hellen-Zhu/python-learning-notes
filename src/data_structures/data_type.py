# 数据类型

# 数字类型: 整数，浮点数，布尔值
age=18
height = 170.1
is_female=True

print(type(age), type(height),type(is_female))

# 非数字类型
name = 'Hellen'
hobbies = '''love sport'''

list1 = [1,2,3]
tuple1 = (1,2,3)
set1 = {1,2,3}
dict1 = {'name':'Hellen','age':18}

print(type(name), type(hobbies), type(list1),type(tuple1),type(set1),type(dict1))

# Python 数据类型详解
"""
Python 中的数据类型可以分为以下几类:

1. 数字类型 (Numeric Types):
   
   a) 整数 (int):
   - 表示整数，可以是正数、负数或零
   - 没有大小限制 (Python 3)
   - 例如: 18, -5, 0, 1000000
   
   b) 浮点数 (float):
   - 表示小数，包含小数点
   - 例如: 170.1, -3.14, 0.0, 2.5e-10

   c) 复数 (complex):
   - 表示复数，包含实部和虚部
   - 例如: 3+4j, -2-5j, 1j
   
   d) 布尔值 (bool):
   - 表示真或假
   - 只有两个值: True 和 False
   - 是 int 的子类 (True=1, False=0)

2. 字符串类型 (String):
   
   a) 字符串 (str):
   - 表示文本数据
   - 用单引号、双引号或三引号包围
   - 不可变类型
   - 例如: 'Hellen', "Hello World", '''多行字符串'''

3. 序列类型 (Sequence Types):
   
   a) 列表 (list):
   - 有序的可变序列
   - 用方括号 [] 表示
   - 可以包含不同类型的元素
   - 例如: [1, 2, 3], ['a', 'b', 'c'], [1, 'hello', 3.14]
   
   b) 元组 (tuple):
   - 有序的不可变序列
   - 用圆括号 () 表示
   - 创建后不能修改
   - 例如: (1, 2, 3), ('a', 'b', 'c'), (1, 'hello', 3.14)
   
   c) 范围 (range):
   - 表示一个数字序列
   - 常用于循环
   - 例如: range(5), range(1, 10), range(0, 10, 2)

4. 集合类型 (Set Types):
   
   a) 集合 (set):
   - 无序的不重复元素集合
   - 用花括号 {} 表示
   - 可变类型
   - 例如: {1, 2, 3}, {'a', 'b', 'c'}
   
   b) 不可变集合 (frozenset):
   - 不可变的集合
   - 例如: frozenset([1, 2, 3])

5. 映射类型 (Mapping Types):
   
   a) 字典 (dict):
   - 键值对的无序集合
   - 用花括号 {} 表示，键值对用冒号分隔
   - 键必须是不可变类型
   - 例如: {'name': 'Hellen', 'age': 18}

6. 其他类型:
   
   a) 空值 (None):
   - 表示空值或未定义
   - 只有一个值: None
   
   b) 字节 (bytes):
   - 不可变的字节序列
   - 例如: b'Hello'
   
   c) 字节数组 (bytearray):
   - 可变的字节序列
   - 例如: bytearray(b'Hello')
   
   d) 内存视图 (memoryview):
   - 内存中对象的视图
   - 用于内存操作

7. 类型检查方法:
   
   a) type() 函数:
   - 返回对象的类型
   - 例如: type(18) 返回 <class 'int'>
   
   b) isinstance() 函数:
   - 检查对象是否为指定类型
   - 例如: isinstance(18, int) 返回 True

8. 数据类型的特点:
   
   a) 可变类型 (Mutable):
   - 列表 (list)
   - 字典 (dict)
   - 集合 (set)
   - 字节数组 (bytearray)
   
   b) 不可变类型 (Immutable):
   - 数字 (int, float, complex)
   - 字符串 (str)
   - 元组 (tuple)
   - 不可变集合 (frozenset)
   - 字节 (bytes)

9. 实际应用示例:
"""

# 数字类型示例
integer_num = 42
float_num = 3.14
complex_num = 2 + 3j
boolean_val = True

print(f"整数: {integer_num}, 类型: {type(integer_num)}")
print(f"浮点数: {float_num}, 类型: {type(float_num)}")
print(f"复数: {complex_num}, 类型: {type(complex_num)}")
print(f"布尔值: {boolean_val}, 类型: {type(boolean_val)}")

# 字符串类型示例
single_quoted = 'Hello'
double_quoted = "World"
multi_line = """这是一个
多行字符串"""

print(f"单引号字符串: {single_quoted}")
print(f"双引号字符串: {double_quoted}")
print(f"多行字符串: {multi_line}")

# 序列类型示例
my_list = [1, 'hello', 3.14, True]
my_tuple = (1, 'hello', 3.14, True)
my_range = range(5)

print(f"列表: {my_list}, 类型: {type(my_list)}")
print(f"元组: {my_tuple}, 类型: {type(my_tuple)}")
print(f"范围: {list(my_range)}, 类型: {type(my_range)}")

# 集合类型示例
my_set = {1, 2, 3, 3, 4}  # 重复元素会被自动去除
my_frozenset = frozenset([1, 2, 3])

print(f"集合: {my_set}, 类型: {type(my_set)}")
print(f"不可变集合: {my_frozenset}, 类型: {type(my_frozenset)}")

# 映射类型示例
my_dict = {'name': 'Hellen', 'age': 18, 'city': 'Beijing'}

print(f"字典: {my_dict}, 类型: {type(my_dict)}")

# 类型检查示例
print(f"18 是整数吗? {isinstance(18, int)}")
print(f"'hello' 是字符串吗? {isinstance('hello', str)}")
print(f"[1, 2, 3] 是列表吗? {isinstance([1, 2, 3], list)}")

# 可变性测试
print("\n可变性测试:")
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# 列表是可变的
my_list[0] = 10
print(f"修改后的列表: {my_list}")

# 元组是不可变的 (会报错)
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
print(f"元组保持不变: {my_tuple}")

# 列表、元组、集合、字典的通俗对比
"""
用生活中的例子来理解这四种数据类型:

1. 列表 (List) - 就像购物清单
   特点:
   - 有序的 (按添加顺序排列)
   - 可以重复 (可以买多个苹果)
   - 可以修改 (可以添加、删除、修改物品)
   - 用方括号 [] 表示
   
   生活例子:
   购物清单 = ['苹果', '香蕉', '牛奶', '苹果']  # 可以重复买苹果
   
   操作示例:
   - 添加物品: 购物清单.append('面包')
   - 删除物品: 购物清单.remove('香蕉')
   - 修改物品: 购物清单[0] = '橙子'
   - 查看物品: 购物清单[1]  # 查看第二个物品

2. 元组 (Tuple) - 就像身份证信息
   特点:
   - 有序的 (姓名、性别、出生日期、地址)
   - 可以重复 (地址可能有重复)
   - 不可修改 (身份证信息不能随意更改)
   - 用圆括号 () 表示
   
   生活例子:
   身份证信息 = ('张三', '男', '1990-01-01', '北京市朝阳区')
   
   操作示例:
   - 查看信息: 身份证信息[0]  # 查看姓名
   - 不能修改: 身份证信息[0] = '李四'  # 会报错！
   - 可以复制: 新身份证 = 身份证信息

3. 集合 (Set) - 就像朋友聚会名单
   特点:
   - 无序的 (谁先到谁后到不重要)
   - 不能重复 (同一个人不会重复邀请)
   - 可以修改 (可以添加或删除朋友)
   - 用花括号 {} 表示
   
   生活例子:
   聚会名单 = {'张三', '李四', '王五', '赵六'}
   
   操作示例:
   - 添加朋友: 聚会名单.add('孙七')
   - 删除朋友: 聚会名单.remove('李四')
   - 检查是否在: '张三' in 聚会名单  # 返回 True
   - 自动去重: 如果添加已存在的朋友，不会重复

4. 字典 (Dict) - 就像通讯录
   特点:
   - 无序的 (按姓名查找，顺序不重要)
   - 键值对 (姓名对应电话号码)
   - 键不能重复 (一个人只能有一个号码)
   - 可以修改 (可以添加、删除、修改联系人)
   - 用花括号 {} 表示，键值对用冒号分隔
   
   生活例子:
   通讯录 = {'张三': '13800138000', '李四': '13900139000', '王五': '13700137000'}
   
   操作示例:
   - 添加联系人: 通讯录['赵六'] = '13600136000'
   - 修改号码: 通讯录['张三'] = '13800138001'
   - 删除联系人: del 通讯录['李四']
   - 查找号码: 通讯录['王五']  # 返回 '13700137000'

5. 实际对比示例:
"""

print("\n=== 列表、元组、集合、字典对比示例 ===")

# 列表示例 - 购物清单
print("\n1. 列表 (购物清单):")
shopping_list = ['苹果', '香蕉', '牛奶', '苹果']  # 可以重复
print(f"原始清单: {shopping_list}")
shopping_list.append('面包')  # 添加物品
print(f"添加面包后: {shopping_list}")
shopping_list[0] = '橙子'  # 修改第一个物品
print(f"修改第一个物品后: {shopping_list}")
print(f"第二个物品是: {shopping_list[1]}")

# 元组示例 - 身份证信息
print("\n2. 元组 (身份证信息):")
id_info = ('张三', '男', '1990-01-01', '北京市朝阳区')
print(f"身份证信息: {id_info}")
print(f"姓名: {id_info[0]}")
print(f"性别: {id_info[1]}")
# id_info[0] = '李四'  # 这会报错！元组不能修改
print("注意: 元组不能修改，所以身份证信息是固定的")

# 集合示例 - 聚会名单
print("\n3. 集合 (聚会名单):")
party_guests = {'张三', '李四', '王五', '赵六'}
print(f"原始名单: {party_guests}")
party_guests.add('孙七')  # 添加新朋友
print(f"添加孙七后: {party_guests}")
party_guests.add('张三')  # 尝试添加重复的朋友
print(f"尝试添加重复的张三后: {party_guests}")  # 不会重复
party_guests.remove('李四')  # 删除朋友
print(f"删除李四后: {party_guests}")
print(f"张三是否在名单中: {'张三' in party_guests}")

# 字典示例 - 通讯录
print("\n4. 字典 (通讯录):")
phonebook = {'张三': '13800138000', '李四': '13900139000', '王五': '13700137000'}
print(f"原始通讯录: {phonebook}")
phonebook['赵六'] = '13600136000'  # 添加新联系人
print(f"添加赵六后: {phonebook}")
phonebook['张三'] = '13800138001'  # 修改张三的号码
print(f"修改张三号码后: {phonebook}")
print(f"王五的号码是: {phonebook['王五']}")
del phonebook['李四']  # 删除李四
print(f"删除李四后: {phonebook}")

# 使用场景总结
print("\n=== 使用场景总结 ===")
print("""
什么时候使用哪种数据类型:

1. 列表 (List):
   - 当你需要有序的数据集合
   - 需要频繁添加、删除、修改数据
   - 例如: 待办事项、购物清单、学生名单

2. 元组 (Tuple):
   - 当你需要不可变的数据集合
   - 数据一旦创建就不应该改变
   - 例如: 坐标点、日期时间、配置信息

3. 集合 (Set):
   - 当你需要去重的数据集合
   - 不需要关心顺序
   - 例如: 用户标签、兴趣爱好、权限列表

4. 字典 (Dict):
   - 当你需要键值对关系
   - 需要通过键快速查找值
   - 例如: 用户信息、配置参数、缓存数据
""")

# 性能对比
print("\n=== 性能特点 ===")
print("""
性能特点对比:

1. 列表:
   - 查找: 较慢 (需要遍历)
   - 插入/删除: 中等 (需要移动元素)
   - 内存: 中等

2. 元组:
   - 查找: 较慢 (需要遍历)
   - 插入/删除: 不支持
   - 内存: 最少 (不可变)

3. 集合:
   - 查找: 很快 (哈希表)
   - 插入/删除: 很快
   - 内存: 较多

4. 字典:
   - 查找: 很快 (哈希表)
   - 插入/删除: 很快
   - 内存: 最多
""")


