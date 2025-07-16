# ===========================================
# Python 运算符详解
# ===========================================

print("=" * 50)
print("Python 运算符类型详解")
print("=" * 50)

# ===========================================
# 1. 算术运算符 (Arithmetic Operators)
# ===========================================
print("\n1. 算术运算符 (Arithmetic Operators)")
print("-" * 40)

# 加法运算符 (+)
print("加法 (+):")
print(f"2 + 3 = {2+3}")  # 输出: 5

# 减法运算符 (-)
print("减法 (-):")
print(f"3 - 2 = {3-2}")  # 输出: 1

# 乘法运算符 (*)
print("乘法 (*):")
print(f"2 * 3 = {2*3}")  # 输出: 6

# 除法运算符 (/)
print("除法 (/):")
print(f"9 / 2 = {9/2}")  # 输出: 4.5 (浮点数除法)

# 整除运算符 (//)
print("整除 (//):")
print(f"9 // 2 = {9//2}")  # 输出: 4 (整数除法，向下取整)

# 取模运算符 (%)
print("取模 (%):")
print(f"9 % 2 = {9%2}")  # 输出: 1 (求余数)

# 幂运算符 (**)
print("幂运算 (**):")
print(f"2 ** 3 = {2**3}")  # 输出: 8 (2的3次方)
print(f"3 ** 2 = {3**2}")  # 输出: 9 (3的2次方)

# ===========================================
# 2. 比较运算符 (Comparison Operators)
# ===========================================
print("\n2. 比较运算符 (Comparison Operators)")
print("-" * 40)

# 大于 (>)
print("大于 (>):")
print(f"2 > 3 = {2>3}")  # 输出: False

# 小于 (<)
print("小于 (<):")
print(f"2 < 3 = {2<3}")  # 输出: True

# 大于等于 (>=)
print("大于等于 (>=):")
print(f"2 >= 3 = {2>=3}")  # 输出: False
print(f"3 >= 3 = {3>=3}")  # 输出: True

# 小于等于 (<=)
print("小于等于 (<=):")
print(f"2 <= 3 = {2<=3}")  # 输出: True
print(f"3 <= 3 = {3<=3}")  # 输出: True

# 等于 (==)
print("等于 (==):")
print(f"2 == 3 = {2==3}")  # 输出: False
print(f"3 == 3 = {3==3}")  # 输出: True

# 不等于 (!=)
print("不等于 (!=):")
print(f"2 != 3 = {2!=3}")  # 输出: True
print(f"3 != 3 = {3!=3}")  # 输出: False

# ===========================================
# 3. 逻辑运算符 (Logical Operators)
# ===========================================
print("\n3. 逻辑运算符 (Logical Operators)")
print("-" * 40)

# 逻辑与 (and)
print("逻辑与 (and):")
print(f"True and False = {True and False}")  # 输出: False
print(f"True and True = {True and True}")    # 输出: True
print(f"False and False = {False and False}")  # 输出: False

# 逻辑或 (or)
print("逻辑或 (or):")
print(f"True or False = {True or False}")    # 输出: True
print(f"True or True = {True or True}")      # 输出: True
print(f"False or False = {False or False}")  # 输出: False

# 逻辑非 (not)
print("逻辑非 (not):")
print(f"not True = {not True}")    # 输出: False
print(f"not False = {not False}")  # 输出: True

# ===========================================
# 4. 赋值运算符 (Assignment Operators)
# ===========================================
print("\n4. 赋值运算符 (Assignment Operators)")
print("-" * 40)

# 基本赋值 (=)
x = 10
print(f"基本赋值: x = 10, x = {x}")

# 加法赋值 (+=)
x += 5  # 等价于 x = x + 5
print(f"加法赋值: x += 5, x = {x}")

# 减法赋值 (-=)
x -= 3  # 等价于 x = x - 3
print(f"减法赋值: x -= 3, x = {x}")

# 乘法赋值 (*=)
x *= 2  # 等价于 x = x * 2
print(f"乘法赋值: x *= 2, x = {x}")

# 除法赋值 (/=)
x /= 4  # 等价于 x = x / 4
print(f"除法赋值: x /= 4, x = {x}")

# 整除赋值 (//=)
x //= 2  # 等价于 x = x // 2
print(f"整除赋值: x //= 2, x = {x}")

# 取模赋值 (%=)
x %= 3  # 等价于 x = x % 3
print(f"取模赋值: x %= 3, x = {x}")

# 幂赋值 (**=)
x **= 3  # 等价于 x = x ** 3
print(f"幂赋值: x **= 3, x = {x}")

# ===========================================
# 5. 位运算符 (Bitwise Operators)
# ===========================================
print("\n5. 位运算符 (Bitwise Operators)")
print("-" * 40)

a = 60  # 二进制: 00111100
b = 13  # 二进制: 00001101

# 按位与 (&)
print(f"按位与 (&): {a} & {b} = {a & b}")  # 输出: 12 (00001100)

# 按位或 (|)
print(f"按位或 (|): {a} | {b} = {a | b}")  # 输出: 61 (00111101)

# 按位异或 (^)
print(f"按位异或 (^): {a} ^ {b} = {a ^ b}")  # 输出: 49 (00110001)

# 按位取反 (~)
print(f"按位取反 (~): ~{a} = {~a}")  # 输出: -61

# 左移 (<<)
print(f"左移 (<<): {a} << 2 = {a << 2}")  # 输出: 240 (11110000)

# 右移 (>>)
print(f"右移 (>>): {a} >> 2 = {a >> 2}")  # 输出: 15 (00001111)

# ===========================================
# 6. 成员运算符 (Membership Operators)
# ===========================================
print("\n6. 成员运算符 (Membership Operators)")
print("-" * 40)

list_example = [1, 2, 3, 4, 5]
string_example = "Hello Python"

# in 运算符
print(f"in 运算符:")
print(f"3 in {list_example} = {3 in list_example}")  # 输出: True
print(f"'Python' in '{string_example}' = {'Python' in string_example}")  # 输出: True

# not in 运算符
print(f"not in 运算符:")
print(f"6 not in {list_example} = {6 not in list_example}")  # 输出: True
print(f"'Java' not in '{string_example}' = {'Java' not in string_example}")  # 输出: True

# ===========================================
# 7. 身份运算符 (Identity Operators)
# ===========================================
print("\n7. 身份运算符 (Identity Operators)")
print("-" * 40)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

# is 运算符 (检查是否是同一个对象)
print(f"is 运算符:")
print(f"x is z = {x is z}")  # 输出: True (同一个对象)
print(f"x is y = {x is y}")  # 输出: False (不同对象，内容相同)

# is not 运算符
print(f"is not 运算符:")
print(f"x is not y = {x is not y}")  # 输出: True

# ===========================================
# 8. 运算符优先级
# ===========================================
print("\n8. 运算符优先级 (Operator Precedence)")
print("-" * 40)

# 优先级示例
result1 = 2 + 3 * 4  # 先乘后加
result2 = (2 + 3) * 4  # 先括号内，再乘
result3 = 2 ** 3 + 1  # 先幂运算，后加

print(f"2 + 3 * 4 = {result1}")  # 输出: 14
print(f"(2 + 3) * 4 = {result2}")  # 输出: 20
print(f"2 ** 3 + 1 = {result3}")  # 输出: 9

print("\n" + "=" * 50)
print("运算符详解完成！")
print("=" * 50)
