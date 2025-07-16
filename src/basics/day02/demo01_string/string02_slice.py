# ===========================================
# Python 字符串切片详解
# ===========================================

print("=" * 50)
print("Python 字符串切片详解")
print("=" * 50)

# ===========================================
# 1. 字符串切片基础语法
# ===========================================
print("\n1. 字符串切片基础语法")
print("-" * 40)

'''
字符串切片语法:
    string[start:end:step]
    
参数说明:
    start: 起始索引（包含），默认为0
    end: 结束索引（不包含），默认为字符串长度
    step: 步长（可选），默认为1
    
索引规则:
    正索引:从左到右，从0开始
    负索引:从右到左，从-1开始
'''

# 创建示例字符串
text = "Python Programming"
print(f"示例字符串: '{text}'")
print(f"字符串长度: {len(text)}")
print(f"字符索引: {[f'{i}:{text[i]}' for i in range(len(text))]}")

# ===========================================
# 2. 基本切片操作
# ===========================================
print("\n2. 基本切片操作")
print("-" * 40)

# 2.1 正索引切片
print("2.1 正索引切片:")
print(f"前6个字符: text[0:6] = '{text[0:6]}'")
print(f"第2到第8个字符: text[2:8] = '{text[2:8]}'")
print(f"从第7个字符到末尾: text[7:] = '{text[7:]}'")
print(f"从开头到第5个字符: text[:5] = '{text[:5]}'")

# 2.2 负索引切片
print("\n2.2 负索引切片:")
print(f"最后5个字符: text[-5:] = '{text[-5:]}'")
print(f"从开头到倒数第6个字符: text[:-5] = '{text[:-5]}'")
print(f"倒数第8个到倒数第3个字符: text[-8:-3] = '{text[-8:-3]}'")

# 2.3 省略索引
print("\n2.3 省略索引:")
print(f"整个字符串: text[:] = '{text[:]}'")
print(f"从第3个字符开始: text[3:] = '{text[3:]}'")
print(f"到第10个字符结束: text[:10] = '{text[:10]}'")

# ===========================================
# 3. 步长切片
# ===========================================
print("\n3. 步长切片")
print("-" * 40)

# 3.1 正步长
print("3.1 正步长:")
print(f"每隔一个字符: text[::2] = '{text[::2]}'")
print(f"从第1个开始，每隔2个字符: text[1::2] = '{text[1::2]}'")
print(f"前10个字符，每隔3个: text[:10:3] = '{text[:10:3]}'")

# 3.2 负步长（反向切片）
print("\n3.2 负步长（反向切片）:")
print(f"反转字符串: text[::-1] = '{text[::-1]}'")
print(f"从后往前，每隔2个字符: text[::-2] = '{text[::-2]}'")
print(f"从倒数第5个开始，每隔2个字符: text[-5::-2] = '{text[-5::-2]}'")

# 3.3 复杂步长切片
print("\n3.3 复杂步长切片:")
print(f"从第2个到第12个，每隔3个字符: text[2:12:3] = '{text[2:12:3]}'")
print(f"从倒数第10个到倒数第2个，每隔2个字符: text[-10:-2:2] = '{text[-10:-2:2]}'")

# ===========================================
# 4. 切片边界处理
# ===========================================
print("\n4. 切片边界处理")
print("-" * 40)

# 4.1 超出边界的索引
print("4.1 超出边界的索引:")
print(f"索引超出范围: text[0:100] = '{text[0:100]}'")  # 不会报错，返回整个字符串
print(f"负索引超出范围: text[-100:] = '{text[-100:]}'")  # 不会报错，返回整个字符串

# 4.2 空切片
print("\n4.2 空切片:")
print(f"起始索引等于结束索引: text[5:5] = '{text[5:5]}'")  # 空字符串
print(f"起始索引大于结束索引（正步长）: text[10:5] = '{text[10:5]}'")  # 空字符串
print(f"起始索引小于结束索引（负步长）: text[5:10:-1] = '{text[5:10:-1]}'")  # 空字符串

# ===========================================
# 5. 实际应用场景
# ===========================================
print("\n5. 实际应用场景")
print("-" * 40)

# 5.1 提取文件名和扩展名
print("5.1 提取文件名和扩展名:")
file_path = "document.txt"
print(f"文件路径: '{file_path}'")

# 方法1:使用rfind()
dot_index = file_path.rfind('.')
if dot_index != -1:
    filename = file_path[:dot_index]
    extension = file_path[dot_index+1:]
    print(f"文件名: '{filename}'")
    print(f"扩展名: '{extension}'")

# 方法2:使用split()
parts = file_path.split('.')
if len(parts) > 1:
    filename = '.'.join(parts[:-1])
    extension = parts[-1]
    print(f"文件名: '{filename}'")
    print(f"扩展名: '{extension}'")

# 5.2 提取URL的不同部分
print("\n5.2 提取URL的不同部分:")
url = "https://www.example.com/path/to/page"
print(f"URL: '{url}'")

# 提取协议
protocol_end = url.find('://')
if protocol_end != -1:
    protocol = url[:protocol_end]
    print(f"协议: '{protocol}'")

# 提取域名
domain_start = protocol_end + 3
domain_end = url.find('/', domain_start)
if domain_end != -1:
    domain = url[domain_start:domain_end]
    print(f"域名: '{domain}'")
    path = url[domain_end:]
    print(f"路径: '{path}'")

# 5.3 字符串反转和回文检查
print("\n5.3 字符串反转和回文检查:")
def is_palindrome(text):
    """检查字符串是否为回文"""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

test_strings = ["racecar", "A man a plan a canal Panama", "hello", "上海自来水来自海上"]
for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' 是回文: {result}")

# 5.4 提取子字符串
print("\n5.4 提取子字符串:")
email = "user@example.com"
print(f"邮箱: '{email}'")

# 提取用户名
at_index = email.find('@')
if at_index != -1:
    username = email[:at_index]
    print(f"用户名: '{username}'")

# 提取域名
domain_part = email[at_index+1:]
dot_index = domain_part.find('.')
if dot_index != -1:
    domain = domain_part[:dot_index]
    print(f"域名: '{domain}'")

# ===========================================
# 6. 高级切片技巧
# ===========================================
print("\n6. 高级切片技巧")
print("-" * 40)

# 6.1 字符串分段
print("6.1 字符串分段:")
long_text = "Python is a powerful programming language"
print(f"原文本: '{long_text}'")

# 每8个字符分段
chunk_size = 8
chunks = [long_text[i:i+chunk_size] for i in range(0, len(long_text), chunk_size)]
print(f"每{chunk_size}个字符分段: {chunks}")

# 6.2 提取单词
print("\n6.2 提取单词:")
sentence = "Python is awesome"
print(f"句子: '{sentence}'")

# 使用切片提取单词（简单方法）
words = sentence.split()
print(f"单词列表: {words}")

# 6.3 字符串填充和对齐
print("\n6.3 字符串填充和对齐:")
short_text = "Hi"
print(f"原文本: '{short_text}'")

# 使用切片实现左对齐
padded_left = short_text + " " * (10 - len(short_text))
print(f"左对齐（10字符）: '{padded_left}'")

# 使用切片实现右对齐
padded_right = " " * (10 - len(short_text)) + short_text
print(f"右对齐（10字符）: '{padded_right}'")

# 使用切片实现居中对齐
left_pad = (10 - len(short_text)) // 2
right_pad = 10 - len(short_text) - left_pad
padded_center = " " * left_pad + short_text + " " * right_pad
print(f"居中对齐（10字符）: '{padded_center}'")

# ===========================================
# 7. 切片性能优化
# ===========================================
print("\n7. 切片性能优化")
print("-" * 40)

# 7.1 避免不必要的切片
print("7.1 避免不必要的切片:")
text = "Hello World"

# 不好的做法
if text[:5] == "Hello":
    print("找到Hello（使用切片）")

# 好的做法
if text.startswith("Hello"):
    print("找到Hello（使用startswith）")

# 7.2 使用切片进行字符串比较
print("\n7.2 使用切片进行字符串比较:")
def compare_strings(str1, str2, start=0, end=None):
    """比较两个字符串的指定部分"""
    if end is None:
        end = min(len(str1), len(str2))
    return str1[start:end] == str2[start:end]

result1 = compare_strings("Hello World", "Hello Python", 0, 5)
result2 = compare_strings("Hello World", "Hello Python", 6)
print(f"前5个字符相同: {result1}")
print(f"从第6个字符开始不同: {result2}")

# ===========================================
# 8. 常见错误和注意事项
# ===========================================
print("\n8. 常见错误和注意事项")
print("-" * 40)

# 8.1 索引越界
print("8.1 索引越界:")
try:
    char = text[100]  # 这会报错
    print(char)
except IndexError as e:
    print(f"索引越界错误: {e}")

# 但切片不会报错
safe_slice = text[100:200]
print(f"安全切片: '{safe_slice}'")

# 8.2 步长为0
print("\n8.2 步长为0:")
try:
    invalid_slice = text[::0]  # 这会报错
    print(invalid_slice)
except ValueError as e:
    print(f"步长为0错误: {e}")

# 8.3 浮点数索引
print("\n8.3 浮点数索引:")
try:
    float_slice = text[1.5:3.5]  # 这会报错
    print(float_slice)
except TypeError as e:
    print(f"浮点数索引错误: {e}")

print("\n" + "=" * 50)
print("字符串切片详解完成！")
print("=" * 50)
