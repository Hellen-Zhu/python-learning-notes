# ===========================================
# Python 字符串详解
# ===========================================

print("=" * 50)
print("Python 字符串定义和常用方法详解")
print("=" * 50)

# ===========================================
# 1. 字符串的定义和创建
# ===========================================
print("\n1. 字符串的定义和创建")
print("-" * 40)

'''
字符串定义：
    字符串是不可变的字符序列，一旦创建就不能修改
    字符串是Python中最常用的数据类型之一
'''

# 1.1 单引号创建字符串
print("1.1 单引号创建字符串:")
str1 = 'hello'
print(f"str1 = '{str1}', 类型: {type(str1)}")

# 1.2 双引号创建字符串
print("\n1.2 双引号创建字符串:")
str2 = "hello"
print(f"str2 = \"{str2}\", 类型: {type(str2)}")

# 1.3 三引号创建字符串（多行字符串）
print("\n1.3 三引号创建字符串（多行字符串）:")
str3 = '''hello
world
python'''
str4 = """hello
world
python"""
print(f"str3:\n{str3}")
print(f"str4:\n{str4}")

# 1.4 字符串的不可变性
print("\n1.4 字符串的不可变性:")
# str1[0] = 'H'  # 这会报错：TypeError: 'str' object does not support item assignment
print("字符串是不可变的，不能直接修改单个字符")

# ===========================================
# 2. 转义字符
# ===========================================
print("\n2. 转义字符")
print("-" * 40)

# 2.1 常用转义字符
print("2.1 常用转义字符:")
str5 = 'hello\nworld'      # \n 换行
print(f"换行符: '{str5}'")

str6 = "hello\tworld"      # \t 制表符
print(f"制表符: '{str6}'")

str7 = "hello\\world"      # \\ 反斜杠
print(f"反斜杠: '{str7}'")

str8 = "hello\bworld"      # \b 退格
print(f"退格符: '{str8}'")

str9 = "hello\rworld"      # \r 回车
print(f"回车符: '{str9}'")

# 2.2 引号转义
print("\n2.2 引号转义:")
str10 = "I'm a student"    # 双引号包含单引号
print(f"双引号包含单引号: '{str10}'")

str11 = 'I\'m a student'   # 单引号转义
print(f"单引号转义: '{str11}'")

str12 = 'I\\\'m a student' # 多重转义
print(f"多重转义: '{str12}'")

# 2.3 原始字符串（raw string）
print("\n2.3 原始字符串（raw string）:")
str13 = r'I\'m a student'  # r前缀，不处理转义字符
print(f"原始字符串: '{str13}'")

# ===========================================
# 3. 字符串的常用方法
# ===========================================
print("\n3. 字符串的常用方法")
print("-" * 40)

# 3.1 字符串长度
print("3.1 字符串长度:")
text = "Hello World"
print(f"字符串: '{text}'")
print(f"长度: {len(text)}")

# 3.2 字符串索引和切片
print("\n3.2 字符串索引和切片:")
print(f"第一个字符: {text[0]}")
print(f"最后一个字符: {text[-1]}")
print(f"前5个字符: {text[:5]}")
print(f"后5个字符: {text[-5:]}")
print(f"中间字符: {text[2:7]}")

# 3.3 字符串查找
print("\n3.3 字符串查找:")
print(f"查找'World': {text.find('World')}")
print(f"查找'Python': {text.find('Python')}")  # 找不到返回-1
print(f"查找'o'的位置: {text.index('o')}")
print(f"从右侧查找'o': {text.rfind('o')}")

# 3.4 字符串替换
print("\n3.4 字符串替换:")
new_text = text.replace('World', 'Python')
print(f"原字符串: '{text}'")
print(f"替换后: '{new_text}'")

# 3.5 字符串分割
print("\n3.5 字符串分割:")
words = text.split()
print(f"按空格分割: {words}")
csv_text = "apple,banana,orange"
fruits = csv_text.split(',')
print(f"按逗号分割: {fruits}")

# 3.6 字符串连接
print("\n3.6 字符串连接:")
joined = ' '.join(words)
print(f"连接后的字符串: '{joined}'")

# 3.7 字符串大小写转换
print("\n3.7 字符串大小写转换:")
print(f"转大写: {text.upper()}")
print(f"转小写: {text.lower()}")
print(f"首字母大写: {text.capitalize()}")
print(f"每个单词首字母大写: {text.title()}")

# 3.8 字符串去除空白
print("\n3.8 字符串去除空白:")
whitespace_text = "  Hello World  "
print(f"原字符串: '{whitespace_text}'")
print(f"去除两端空白: '{whitespace_text.strip()}'")
print(f"去除左侧空白: '{whitespace_text.lstrip()}'")
print(f"去除右侧空白: '{whitespace_text.rstrip()}'")

# 3.9 字符串判断方法
print("\n3.9 字符串判断方法:")
print(f"是否以'Hello'开头: {text.startswith('Hello')}")
print(f"是否以'World'结尾: {text.endswith('World')}")
print(f"是否全为字母: {text.isalpha()}")
print(f"是否全为数字: {'123'.isdigit()}")
print(f"是否全为字母数字: {text.isalnum()}")
print(f"是否全为小写: {text.islower()}")
print(f"是否全为大写: {text.isupper()}")

# 3.10 字符串格式化
print("\n3.10 字符串格式化:")
name = "张三"
age = 25
# 使用format()方法
formatted1 = "我叫{}，今年{}岁".format(name, age)
print(f"format()方法: {formatted1}")

# 使用f-string（推荐）
formatted2 = f"我叫{name}，今年{age}岁"
print(f"f-string方法: {formatted2}")

# 使用%操作符
formatted3 = "我叫%s，今年%d岁" % (name, age)
print(f"%操作符: {formatted3}")

# ===========================================
# 4. 字符串的高级操作
# ===========================================
print("\n4. 字符串的高级操作")
print("-" * 40)

# 4.1 字符串重复
print("4.1 字符串重复:")
repeated = "Ha" * 3
print(f"重复字符串: '{repeated}'")

# 4.2 字符串比较
print("\n4.2 字符串比较:")
str_a = "apple"
str_b = "banana"
print(f"'{str_a}' < '{str_b}': {str_a < str_b}")
print(f"'{str_a}' == '{str_b}': {str_a == str_b}")

# 4.3 字符串包含判断
print("\n4.3 字符串包含判断:")
print(f"'Hello' in '{text}': {'Hello' in text}")
print(f"'Python' in '{text}': {'Python' in text}")

# 4.4 字符串计数
print("\n4.4 字符串计数:")
count_text = "hello hello hello"
print(f"字符串: '{count_text}'")
print(f"'hello'出现次数: {count_text.count('hello')}")
print(f"'o'出现次数: {count_text.count('o')}")

# 4.5 字符串对齐
print("\n4.5 字符串对齐:")
align_text = "Python"
print(f"左对齐: '{align_text.ljust(10)}'")
print(f"右对齐: '{align_text.rjust(10)}'")
print(f"居中对齐: '{align_text.center(10)}'")

# ===========================================
# 5. 实际应用示例
# ===========================================
print("\n5. 实际应用示例")
print("-" * 40)

# 5.1 用户输入处理
print("5.1 用户输入处理:")
user_input = "  hello world  "
cleaned_input = user_input.strip().title()
print(f"原始输入: '{user_input}'")
print(f"处理后: '{cleaned_input}'")

# 5.2 文件路径处理
print("\n5.2 文件路径处理:")
file_path = "/home/user/documents/file.txt"
filename = file_path.split('/')[-1]
extension = filename.split('.')[-1]
print(f"文件路径: {file_path}")
print(f"文件名: {filename}")
print(f"文件扩展名: {extension}")

# 5.3 数据验证
print("\n5.3 数据验证:")
email = "user@example.com"
phone = "1234567890"
print(f"邮箱格式检查: {email.count('@') == 1 and '.' in email}")
print(f"手机号格式检查: {phone.isdigit() and len(phone) == 10}")

print("\n" + "=" * 50)
print("字符串详解完成！")
print("=" * 50)
        
        
        