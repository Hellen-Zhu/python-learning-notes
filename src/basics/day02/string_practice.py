# ===========================================
# Python 字符串练习
# ===========================================

print("🚀 Python 字符串练习")
print("=" * 50)

# ===========================================
# 练习1：字符串基础操作
# ===========================================
print("\n📝 练习1：字符串基础操作")
print("-" * 30)

# 1.1 字符串创建和基本操作
print("1.1 字符串创建和基本操作:")
text = "Python Programming"
print(f"原字符串: '{text}'")
print(f"字符串长度: {len(text)}")
print(f"第一个字符: {text[0]}")
print(f"最后一个字符: {text[-1]}")
print(f"前6个字符: {text[:6]}")
print(f"后10个字符: {text[-10:]}")

# 1.2 字符串拼接
print("\n1.2 字符串拼接:")
first_name = "张三"
last_name = "李"
full_name = last_name + first_name
print(f"姓名拼接: {full_name}")

# 1.3 字符串重复
print("\n1.3 字符串重复:")
separator = "-" * 20
print(f"分隔线: {separator}")

# ===========================================
# 练习2：字符串查找和替换
# ===========================================
print("\n📝 练习2：字符串查找和替换")
print("-" * 30)

# 2.1 查找子字符串
print("2.1 查找子字符串:")
sentence = "Python is a powerful programming language"
print(f"句子: '{sentence}'")
print(f"'Python'的位置: {sentence.find('Python')}")
print(f"'Java'的位置: {sentence.find('Java')}")  # 找不到返回-1
print(f"'programming'的位置: {sentence.index('programming')}")

# 2.2 替换字符串
print("\n2.2 替换字符串:")
new_sentence = sentence.replace('Python', 'Java')
print(f"替换后: '{new_sentence}'")

# 2.3 多次替换
print("\n2.3 多次替换:")
text_with_spaces = "hello   world   python"
cleaned_text = text_with_spaces.replace('   ', ' ')
print(f"原文本: '{text_with_spaces}'")
print(f"清理后: '{cleaned_text}'")

# ===========================================
# 练习3：字符串分割和连接
# ===========================================
print("\n📝 练习3：字符串分割和连接")
print("-" * 30)

# 3.1 字符串分割
print("3.1 字符串分割:")
csv_data = "apple,banana,orange,grape,kiwi"
fruits = csv_data.split(',')
print(f"CSV数据: '{csv_data}'")
print(f"分割后: {fruits}")

# 3.2 多行文本分割
print("\n3.2 多行文本分割:")
multi_line = "第一行\n第二行\n第三行"
lines = multi_line.split('\n')
print(f"多行文本:\n{multi_line}")
print(f"分割后: {lines}")

# 3.3 字符串连接
print("\n3.3 字符串连接:")
words = ['Python', 'is', 'awesome']
joined_text = ' '.join(words)
print(f"单词列表: {words}")
print(f"连接后: '{joined_text}'")

# 3.4 自定义分隔符连接
print("\n3.4 自定义分隔符连接:")
numbers = ['1', '2', '3', '4', '5']
number_string = '-'.join(numbers)
print(f"数字列表: {numbers}")
print(f"连接后: '{number_string}'")

# ===========================================
# 练习4：字符串大小写和格式化
# ===========================================
print("\n📝 练习4：字符串大小写和格式化")
print("-" * 30)

# 4.1 大小写转换
print("4.1 大小写转换:")
mixed_text = "Hello World Python"
print(f"原文本: '{mixed_text}'")
print(f"转大写: '{mixed_text.upper()}'")
print(f"转小写: '{mixed_text.lower()}'")
print(f"首字母大写: '{mixed_text.capitalize()}'")
print(f"每个单词首字母大写: '{mixed_text.title()}'")

# 4.2 字符串格式化
print("\n4.2 字符串格式化:")
name = "李四"
age = 28
city = "北京"
job = "程序员"

# 使用f-string
intro1 = f"我叫{name}，今年{age}岁，住在{city}，是一名{job}"
print(f"f-string格式化: {intro1}")

# 使用format()方法
intro2 = "我叫{}，今年{}岁，住在{}，是一名{}".format(name, age, city, job)
print(f"format()格式化: {intro2}")

# 使用%操作符
intro3 = "我叫%s，今年%d岁，住在%s，是一名%s" % (name, age, city, job)
print(f"%操作符格式化: {intro3}")

# ===========================================
# 练习5：字符串清理和验证
# ===========================================
print("\n📝 练习5：字符串清理和验证")
print("-" * 30)

# 5.1 去除空白字符
print("5.1 去除空白字符:")
dirty_text = "  \t  Hello World  \n  "
print(f"原文本: '{dirty_text}'")
print(f"去除两端空白: '{dirty_text.strip()}'")
print(f"去除左侧空白: '{dirty_text.lstrip()}'")
print(f"去除右侧空白: '{dirty_text.rstrip()}'")

# 5.2 字符串验证
print("\n5.2 字符串验证:")
test_strings = ["Hello123", "123456", "Hello", "hello", "HELLO", ""]
for s in test_strings:
    print(f"'{s}': 字母={s.isalpha()}, 数字={s.isdigit()}, 字母数字={s.isalnum()}, 空={s == ''}")

# 5.3 前缀和后缀检查
print("\n5.3 前缀和后缀检查:")
filename = "document.txt"
print(f"文件名: '{filename}'")
print(f"是否以'doc'开头: {filename.startswith('doc')}")
print(f"是否以'.txt'结尾: {filename.endswith('.txt')}")

# ===========================================
# 练习6：字符串高级操作
# ===========================================
print("\n📝 练习6：字符串高级操作")
print("-" * 30)

# 6.1 字符串计数
print("6.1 字符串计数:")
count_text = "hello hello hello world"
print(f"文本: '{count_text}'")
print(f"'hello'出现次数: {count_text.count('hello')}")
print(f"'o'出现次数: {count_text.count('o')}")

# 6.2 字符串对齐
print("\n6.2 字符串对齐:")
align_text = "Python"
print(f"原文本: '{align_text}'")
print(f"左对齐(10): '{align_text.ljust(10)}'")
print(f"右对齐(10): '{align_text.rjust(10)}'")
print(f"居中对齐(10): '{align_text.center(10)}'")

# 6.3 字符串包含判断
print("\n6.3 字符串包含判断:")
main_text = "Python is a programming language"
search_terms = ["Python", "Java", "programming", "script"]
for term in search_terms:
    print(f"'{term}' in '{main_text}': {term in main_text}")

# ===========================================
# 练习7：实际应用场景
# ===========================================
print("\n📝 练习7：实际应用场景")
print("-" * 30)

# 7.1 用户输入处理
print("7.1 用户输入处理:")
def process_user_input(user_input):
    """处理用户输入"""
    # 去除空白字符
    cleaned = user_input.strip()
    # 转换为标题格式
    formatted = cleaned.title()
    # 检查是否为空
    if not cleaned:
        return "输入为空"
    return formatted

test_inputs = ["  hello world  ", "python programming", "  ", "JAVA SCRIPT"]
for input_text in test_inputs:
    result = process_user_input(input_text)
    print(f"输入: '{input_text}' -> 输出: '{result}'")

# 7.2 文件路径处理
print("\n7.2 文件路径处理:")
def parse_file_path(file_path):
    """解析文件路径"""
    # 获取文件名
    filename = file_path.split('/')[-1]
    # 获取文件扩展名
    if '.' in filename:
        name, extension = filename.rsplit('.', 1)
    else:
        name, extension = filename, ""
    return {
        'full_path': file_path,
        'filename': filename,
        'name': name,
        'extension': extension
    }

file_paths = [
    "/home/user/documents/file.txt",
    "/var/log/system.log",
    "/tmp/no_extension",
    "relative/path/image.jpg"
]

for path in file_paths:
    result = parse_file_path(path)
    print(f"路径: {result['full_path']}")
    print(f"  文件名: {result['filename']}")
    print(f"  名称: {result['name']}")
    print(f"  扩展名: {result['extension']}")

# 7.3 数据验证
print("\n7.3 数据验证:")
def validate_email(email):
    """验证邮箱格式"""
    return email.count('@') == 1 and '.' in email and email.find('@') < email.rfind('.')

def validate_phone(phone):
    """验证手机号格式（11位数字）"""
    return phone.isdigit() and len(phone) == 11

test_emails = ["user@example.com", "invalid.email", "@example.com", "user@.com"]
test_phones = ["13812345678", "1234567890", "1381234567a", "138123456789"]

print("邮箱验证:")
for email in test_emails:
    print(f"'{email}': {validate_email(email)}")

print("\n手机号验证:")
for phone in test_phones:
    print(f"'{phone}': {validate_phone(phone)}")

# 7.4 文本分析
print("\n7.4 文本分析:")
def analyze_text(text):
    """分析文本"""
    words = text.split()
    char_count = len(text)
    word_count = len(words)
    avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    
    return {
        'characters': char_count,
        'words': word_count,
        'avg_word_length': round(avg_word_length, 2)
    }

sample_text = "Python is a powerful programming language that is widely used in data science and web development"
analysis = analyze_text(sample_text)
print(f"文本: '{sample_text}'")
print(f"字符数: {analysis['characters']}")
print(f"单词数: {analysis['words']}")
print(f"平均单词长度: {analysis['avg_word_length']}")

print("\n" + "=" * 50)
print("🎉 字符串练习完成！")
print("=" * 50) 