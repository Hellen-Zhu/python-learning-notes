# ===========================================
# Python for 循环详解
# ===========================================

print("=" * 50)
print("Python for 循环场景详解")
print("=" * 50)

# ===========================================
# 1. 基本for循环场景
# ===========================================
print("\n1. 基本for循环场景")
print("-" * 40)

# 1.1 遍历列表
print("1.1 遍历列表:")
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
for fruit in fruits:
    print(f"我喜欢吃 {fruit}")

# 1.2 遍历字符串
print("\n1.2 遍历字符串:")
word = "Python"
for char in word:
    print(f"字符: {char}")

# 1.3 遍历元组
print("\n1.3 遍历元组:")
coordinates = (10, 20, 30)
for coord in coordinates:
    print(f"坐标值: {coord}")

# 1.4 遍历集合
print("\n1.4 遍历集合:")
colors = {"红色", "绿色", "蓝色", "黄色"}
for color in colors:
    print(f"颜色: {color}")

# 1.5 遍历字典
print("\n1.5 遍历字典:")
person = {"name": "张三", "age": 25, "city": "北京"}

# 遍历键
print("遍历键:")
for key in person:
    print(f"键: {key}")

# 遍历键值对
print("\n遍历键值对:")
for key, value in person.items():
    print(f"{key}: {value}")

# 只遍历值
print("\n只遍历值:")
for value in person.values():
    print(f"值: {value}")

# ===========================================
# 2. 使用range()的循环场景
# ===========================================
print("\n2. 使用range()的循环场景")
print("-" * 40)

# 2.1 指定次数循环
print("2.1 指定次数循环:")
for i in range(5):
    print(f"第 {i+1} 次循环")

# 2.2 指定范围循环
print("\n2.2 指定范围循环:")
for i in range(1, 6):  # 1到5
    print(f"数字: {i}")

# 2.3 指定步长循环
print("\n2.3 指定步长循环:")
for i in range(0, 10, 2):  # 0,2,4,6,8
    print(f"偶数: {i}")

# 2.4 倒序循环
print("\n2.4 倒序循环:")
for i in range(5, 0, -1):  # 5,4,3,2,1
    print(f"倒序: {i}")

# ===========================================
# 3. 带索引的循环场景
# ===========================================
print("\n3. 带索引的循环场景")
print("-" * 40)

# 3.1 使用enumerate()获取索引
print("3.1 使用enumerate()获取索引:")
students = ["张三", "李四", "王五", "赵六"]
for index, student in enumerate(students):
    print(f"第{index+1}个学生: {student}")

# 3.2 指定起始索引
print("\n3.2 指定起始索引:")
for index, student in enumerate(students, start=1):
    print(f"学生{index}: {student}")

# 3.3 使用range()和len()获取索引
print("\n3.3 使用range()和len()获取索引:")
for i in range(len(students)):
    print(f"索引{i}: {students[i]}")

# ===========================================
# 4. 嵌套循环场景
# ===========================================
print("\n4. 嵌套循环场景")
print("-" * 40)

# 4.1 二维列表遍历
print("4.1 二维列表遍历:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(f"{element}", end=" ")
    print()  # 换行

# 4.2 使用索引的嵌套循环
print("\n4.2 使用索引的嵌套循环:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# 4.3 乘法表
print("\n4.3 乘法表:")
for i in range(1, 4):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end=" ")
    print()

# ===========================================
# 5. 条件控制循环场景
# ===========================================
print("\n5. 条件控制循环场景")
print("-" * 40)

# 5.1 使用continue跳过某些元素
print("5.1 使用continue跳过某些元素:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:  # 跳过偶数
        continue
    print(f"奇数: {num}")

# 5.2 使用break提前结束循环
print("\n5.2 使用break提前结束循环:")
for num in numbers:
    if num == 7:  # 遇到7就停止
        break
    print(f"数字: {num}")

# 5.3 使用else子句
print("\n5.3 使用else子句:")
for num in [1, 2, 3, 4, 5]:
    if num == 6:
        break
    print(f"处理数字: {num}")
else:
    print("循环正常完成，没有遇到break")

# ===========================================
# 6. 列表推导式场景
# ===========================================
print("\n6. 列表推导式场景")
print("-" * 40)

# 6.1 基本列表推导式
print("6.1 基本列表推导式:")
squares = [x**2 for x in range(1, 6)]
print(f"平方数: {squares}")

# 6.2 带条件的列表推导式
print("\n6.2 带条件的列表推导式:")
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

# 6.3 嵌套列表推导式
print("\n6.3 嵌套列表推导式:")
matrix_3x3 = [[i+j for j in range(3)] for i in range(0, 9, 3)]
print("3x3矩阵:")
for row in matrix_3x3:
    print(row)

# ===========================================
# 7. 实际应用场景
# ===========================================
print("\n7. 实际应用场景")
print("-" * 40)

# 7.1 文件处理
print("7.1 文件处理:")
# 模拟文件内容
file_lines = ["第一行", "第二行", "第三行", "第四行"]
for line_num, line in enumerate(file_lines, 1):
    print(f"第{line_num}行: {line}")

# 7.2 数据处理
print("\n7.2 数据处理:")
scores = [85, 92, 78, 96, 88, 75]
total = 0
count = 0
for score in scores:
    total += score
    count += 1
average = total / count
print(f"平均分: {average:.2f}")

# 7.3 字符串处理
print("\n7.3 字符串处理:")
sentence = "Python is a great programming language"
word_count = 0
for char in sentence:
    if char == ' ':
        word_count += 1
word_count += 1  # 最后一个单词
print(f"单词数量: {word_count}")

# 7.4 字典数据处理
print("\n7.4 字典数据处理:")
inventory = {
    "苹果": 10,
    "香蕉": 15,
    "橙子": 8,
    "葡萄": 12
}

# 计算总库存
total_items = 0
for item, quantity in inventory.items():
    total_items += quantity
    print(f"{item}: {quantity}个")

print(f"总库存: {total_items}个")

# ===========================================
# 8. 高级循环技巧
# ===========================================
print("\n8. 高级循环技巧")
print("-" * 40)

# 8.1 使用zip()并行遍历
print("8.1 使用zip()并行遍历:")
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]
cities = ["北京", "上海", "广州"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}今年{age}岁，住在{city}")

# 8.2 使用filter()过滤
print("\n8.2 使用filter()过滤:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {even_numbers}")

# 8.3 使用map()转换
print("\n8.3 使用map()转换:")
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"翻倍: {doubled_numbers}")

# 8.4 生成器表达式
print("\n8.4 生成器表达式:")
# 计算1到100的和
sum_gen = sum(x for x in range(1, 101))
print(f"1到100的和: {sum_gen}")

# ===========================================
# 9. 性能优化技巧
# ===========================================
print("\n9. 性能优化技巧")
print("-" * 40)

# 9.1 使用enumerate()而不是range(len())
print("9.1 使用enumerate()而不是range(len()):")
# 推荐写法
for index, item in enumerate(students):
    print(f"索引{index}: {item}")

# 9.2 使用in检查成员关系
print("\n9.2 使用in检查成员关系:")
if "张三" in students:
    print("张三在学生列表中")

# 9.3 使用any()和all()
print("\n9.3 使用any()和all():")
has_passing_score = any(score >= 60 for score in scores)
all_passing = all(score >= 60 for score in scores)
print(f"有及格分数: {has_passing_score}")
print(f"全部及格: {all_passing}")

print("\n" + "=" * 50)
print("for 循环详解完成！")
print("=" * 50)
