# ===========================================
# Python 字符串切片练习
# ===========================================

print("🚀 Python 字符串切片练习")
print("=" * 50)

# ===========================================
# 练习1:基础切片操作
# ===========================================
print("\n📝 练习1:基础切片操作")
print("-" * 30)

# 1.1 基本切片
print("1.1 基本切片:")
text = "Python Programming Language"
print(f"原字符串: '{text}'")
print(f"长度: {len(text)}")

# 提取不同部分
print(f"前6个字符: '{text[:6]}'")
print(f"后8个字符: '{text[-8:]}'")
print(f"中间部分（第7到第18个）: '{text[7:18]}'")
print(f"每隔2个字符: '{text[::2]}'")
print(f"反转字符串: '{text[::-1]}'")

# 1.2 负索引切片
print("\n1.2 负索引切片:")
print(f"倒数第10个到倒数第3个: '{text[-10:-3]}'")
print(f"从开头到倒数第5个: '{text[:-5]}'")
print(f"从倒数第7个开始: '{text[-7:]}'")

# ===========================================
# 练习2:字符串处理应用
# ===========================================
print("\n📝 练习2:字符串处理应用")
print("-" * 30)

# 2.1 提取文件信息
print("2.1 提取文件信息:")
file_paths = [
    "document.txt",
    "image.jpg",
    "video.mp4",
    "archive.tar.gz",
    "no_extension"
]

for path in file_paths:
    print(f"\n文件路径: '{path}'")
    
    # 提取文件名（不含扩展名）
    last_dot = path.rfind('.')
    if last_dot != -1:
        name = path[:last_dot]
        extension = path[last_dot+1:]
        print(f"  文件名: '{name}'")
        print(f"  扩展名: '{extension}'")
    else:
        print(f"  文件名: '{path}'")
        print(f"  扩展名: 无")

# 2.2 提取邮箱信息
print("\n2.2 提取邮箱信息:")
emails = [
    "user@example.com",
    "john.doe@company.org",
    "test123@subdomain.domain.co.uk"
]

for email in emails:
    print(f"\n邮箱: '{email}'")
    
    # 提取用户名
    at_index = email.find('@')
    if at_index != -1:
        username = email[:at_index]
        domain_part = email[at_index+1:]
        print(f"  用户名: '{username}'")
        print(f"  域名: '{domain_part}'")

# ===========================================
# 练习3:文本分析
# ===========================================
print("\n📝 练习3:文本分析")
print("-" * 30)

# 3.1 单词提取和分析
print("3.1 单词提取和分析:")
sentence = "Python is a powerful programming language for data science"
print(f"句子: '{sentence}'")

# 提取单词
words = sentence.split()
print(f"单词列表: {words}")

# 分析每个单词
for i, word in enumerate(words):
    print(f"  单词{i+1}: '{word}' (长度: {len(word)})")
    if len(word) > 5:
        print(f"    前3个字符: '{word[:3]}'")
        print(f"    后3个字符: '{word[-3:]}'")

# 3.2 回文检查
print("\n3.2 回文检查:")
def check_palindrome(text):
    """检查字符串是否为回文"""
    # 清理字符串（只保留字母数字）
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

test_palindromes = [
    "racecar",
    "A man a plan a canal Panama",
    "hello",
    "上海自来水来自海上",
    "12321"
]

for text in test_palindromes:
    is_pal = check_palindrome(text)
    print(f"'{text}' 是回文: {is_pal}")

# ===========================================
# 练习4:URL解析
# ===========================================
print("\n📝 练习4:URL解析")
print("-" * 30)

# 4.1 解析URL组件
print("4.1 解析URL组件:")
urls = [
    "https://www.example.com/path/to/page",
    "http://localhost:8080/api/users",
    "ftp://ftp.example.org/files/document.pdf"
]

for url in urls:
    print(f"\nURL: '{url}'")
    
    # 提取协议
    protocol_end = url.find('://')
    if protocol_end != -1:
        protocol = url[:protocol_end]
        print(f"  协议: '{protocol}'")
        
        # 提取主机部分
        host_start = protocol_end + 3
        host_end = url.find('/', host_start)
        if host_end != -1:
            host = url[host_start:host_end]
            path = url[host_end:]
            print(f"  主机: '{host}'")
            print(f"  路径: '{path}'")
        else:
            host = url[host_start:]
            print(f"  主机: '{host}'")
            print(f"  路径: '/'")

# ===========================================
# 练习5:字符串格式化
# ===========================================
print("\n📝 练习5:字符串格式化")
print("-" * 30)

# 5.1 创建格式化字符串
print("5.1 创建格式化字符串:")
def create_formatted_string(text, width=20):
    """创建固定宽度的格式化字符串"""
    if len(text) >= width:
        return text[:width-3] + "..."
    else:
        return text + " " * (width - len(text))

test_texts = ["Short", "Medium length text", "Very long text that exceeds the limit"]
for text in test_texts:
    formatted = create_formatted_string(text, 15)
    print(f"'{text}' -> '{formatted}'")

# 5.2 字符串对齐
print("\n5.2 字符串对齐:")
def align_text(text, width=10, alignment='left'):
    """对齐文本"""
    if len(text) >= width:
        return text[:width]
    
    if alignment == 'left':
        return text + " " * (width - len(text))
    elif alignment == 'right':
        return " " * (width - len(text)) + text
    elif alignment == 'center':
        left_pad = (width - len(text)) // 2
        right_pad = width - len(text) - left_pad
        return " " * left_pad + text + " " * right_pad

sample_text = "Hi"
print(f"原文本: '{sample_text}'")
print(f"左对齐: '{align_text(sample_text, 10, 'left')}'")
print(f"右对齐: '{align_text(sample_text, 10, 'right')}'")
print(f"居中对齐: '{align_text(sample_text, 10, 'center')}'")

# ===========================================
# 练习6:高级切片技巧
# ===========================================
print("\n📝 练习6:高级切片技巧")
print("-" * 30)

# 6.1 字符串分段
print("6.1 字符串分段:")
def split_string(text, chunk_size):
    """将字符串按指定大小分段"""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

long_text = "Python is a powerful programming language"
chunks = split_string(long_text, 8)
print(f"原文本: '{long_text}'")
print(f"每8个字符分段: {chunks}")

# 6.2 提取重复模式
print("\n6.2 提取重复模式:")
def find_repeating_pattern(text, pattern_length=3):
    """查找重复的模式"""
    patterns = {}
    for i in range(len(text) - pattern_length + 1):
        pattern = text[i:i+pattern_length]
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1
    
    # 返回出现次数大于1的模式
    return {k: v for k, v in patterns.items() if v > 1}

sample_text = "ababababab"
repeating_patterns = find_repeating_pattern(sample_text, 2)
print(f"文本: '{sample_text}'")
print(f"重复的2字符模式: {repeating_patterns}")

# ===========================================
# 练习7:实际项目应用
# ===========================================
print("\n📝 练习7:实际项目应用")
print("-" * 30)

# 7.1 日志解析
print("7.1 日志解析:")
log_entries = [
    "2024-01-15 10:30:45 [INFO] User login successful",
    "2024-01-15 10:31:12 [ERROR] Database connection failed",
    "2024-01-15 10:32:00 [WARN] High memory usage detected"
]

for log in log_entries:
    print(f"\n日志: '{log}'")
    
    # 提取时间戳
    timestamp = log[:19]
    print(f"  时间戳: '{timestamp}'")
    
    # 提取日志级别
    level_start = log.find('[') + 1
    level_end = log.find(']')
    if level_start > 0 and level_end > level_start:
        level = log[level_start:level_end]
        print(f"  级别: '{level}'")
    
    # 提取消息
    message_start = log.find(']') + 2
    if message_start > 1:
        message = log[message_start:]
        print(f"  消息: '{message}'")

# 7.2 数据清理
print("\n7.2 数据清理:")
def clean_data(data_string):
    """清理数据字符串"""
    # 去除首尾空白
    cleaned = data_string.strip()
    # 去除多余的空格
    cleaned = ' '.join(cleaned.split())
    # 转换为标题格式
    cleaned = cleaned.title()
    return cleaned

dirty_data = [
    "  hello world  ",
    "python   programming   language",
    "  DATA   SCIENCE  ",
    "  "
]

for data in dirty_data:
    cleaned = clean_data(data)
    print(f"'{data}' -> '{cleaned}'")

# 7.3 密码强度检查
print("\n7.3 密码强度检查:")
def check_password_strength(password):
    """检查密码强度"""
    if len(password) < 8:
        return "弱密码:长度不足8位"
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if score == 4:
        return "强密码"
    elif score >= 2:
        return "中等密码"
    else:
        return "弱密码"

passwords = ["abc123", "Password123", "MyP@ssw0rd!", "weak"]
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"密码 '{pwd}': {strength}")

print("\n" + "=" * 50)
print("🎉 字符串切片练习完成！")
print("=" * 50) 