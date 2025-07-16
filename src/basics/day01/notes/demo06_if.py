# ===========================================
# Python if 条件判断练习
# ===========================================

print("🚀 Python if 条件判断练习")
print("=" * 50)

# ===========================================
# 练习1：基础条件判断
# ===========================================
print("\n📝 练习1：基础条件判断")
print("-" * 30)

# 1.1 年龄判断
age = int(input("请输入您的年龄: "))
if age < 0:
    print("年龄不能为负数")
elif age < 18:
    print("未成年人")
elif age < 60:
    print("成年人")
else:
    print("老年人")

# 1.2 成绩等级判断
score = float(input("请输入您的成绩(0-100): "))
if score < 0 or score > 100:
    print("成绩范围错误")
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# ===========================================
# 练习2：复合条件判断
# ===========================================
print("\n📝 练习2：复合条件判断")
print("-" * 30)

# 2.1 登录验证
username = input("请输入用户名: ")
password = input("请输入密码: ")

if username == "admin" and password == "123456":
    print("登录成功！")
elif username == "admin" and password != "123456":
    print("密码错误！")
elif username != "admin":
    print("用户名不存在！")
else:
    print("登录失败！")

# 2.2 购物折扣计算
purchase_amount = float(input("请输入购物金额: "))
is_vip = input("是否是VIP用户(y/n): ").lower() == 'y'
is_holiday = input("是否是节假日(y/n): ").lower() == 'y'

discount = 0
if is_vip and is_holiday:
    discount = 0.3
elif is_vip:
    discount = 0.2
elif is_holiday:
    discount = 0.1
elif purchase_amount >= 1000:
    discount = 0.05

final_amount = purchase_amount * (1 - discount)
print(f"原价: {purchase_amount:.2f}")
print(f"折扣: {discount*100:.0f}%")
print(f"最终价格: {final_amount:.2f}")

# ===========================================
# 练习3：嵌套条件判断
# ===========================================
print("\n📝 练习3：嵌套条件判断")
print("-" * 30)

# 3.1 银行账户操作
account_type = input("账户类型(savings/checking): ").lower()
balance = float(input("账户余额: "))
operation = input("操作类型(deposit/withdraw): ").lower()
amount = float(input("操作金额: "))

if operation == "deposit":
    if amount > 0:
        balance += amount
        print(f"存款成功！新余额: {balance:.2f}")
    else:
        print("存款金额必须大于0")
elif operation == "withdraw":
    if account_type == "savings":
        if balance >= amount and amount <= 50000:
            balance -= amount
            print(f"取款成功！新余额: {balance:.2f}")
        elif amount > 50000:
            print("储蓄账户单日取款限额50000")
        else:
            print("余额不足")
    elif account_type == "checking":
        if balance >= amount:
            balance -= amount
            print(f"取款成功！新余额: {balance:.2f}")
        else:
            print("余额不足")
    else:
        print("账户类型错误")
else:
    print("操作类型错误")

# ===========================================
# 练习4：特殊条件判断
# ===========================================
print("\n📝 练习4：特殊条件判断")
print("-" * 30)

# 4.1 空值检查
user_input = input("请输入一些内容(直接回车表示空): ")
if not user_input:
    print("输入为空")
elif user_input.strip() == "":
    print("输入只包含空格")
else:
    print(f"输入内容: {user_input}")

# 4.2 数据类型检查
value = input("请输入一个数字或字符串: ")
if value.isdigit():
    print("输入的是数字")
elif value.replace(".", "").isdigit():
    print("输入的是浮点数")
elif value.isalpha():
    print("输入的是纯字母")
elif value.isalnum():
    print("输入的是字母数字组合")
else:
    print("输入的是其他类型")

# ===========================================
# 练习5：条件表达式（三元运算符）
# ===========================================
print("\n📝 练习5：条件表达式（三元运算符）")
print("-" * 30)

# 5.1 简单条件表达式
number = int(input("请输入一个数字: "))
result = "偶数" if number % 2 == 0 else "奇数"
print(f"{number} 是 {result}")

# 5.2 嵌套条件表达式
score = float(input("请输入成绩: "))
grade = "优秀" if score >= 90 else "良好" if score >= 80 else "及格" if score >= 60 else "不及格"
print(f"成绩等级: {grade}")

# 5.3 复杂条件表达式
age = int(input("请输入年龄: "))
income = float(input("请输入收入: "))
status = "高收入" if income >= 10000 else "中等收入" if income >= 5000 else "低收入"
can_apply = "可以申请" if age >= 18 and income >= 3000 else "无法申请"
print(f"收入状态: {status}, 信用卡申请: {can_apply}")

# ===========================================
# 练习6：实际应用场景
# ===========================================
print("\n📝 练习6：实际应用场景")
print("-" * 30)

# 6.1 天气穿衣建议
temperature = float(input("请输入当前温度(摄氏度): "))
weather = input("请输入天气状况(sunny/rainy/cloudy): ").lower()
humidity = int(input("请输入湿度(0-100): "))

clothing = []
if temperature < 10:
    clothing.append("厚外套")
elif temperature < 20:
    clothing.append("薄外套")
else:
    clothing.append("短袖")

if weather == "rainy":
    clothing.append("雨伞")
elif weather == "sunny" and temperature > 25:
    clothing.append("遮阳伞")

if humidity > 80:
    clothing.append("注意防潮")

print(f"穿衣建议: {', '.join(clothing)}")

# 6.2 餐厅点餐系统
time = input("请输入当前时间(格式: HH:MM): ")
hour = int(time.split(":")[0])

if 6 <= hour < 11:
    meal_type = "早餐"
    menu = ["包子", "豆浆", "油条", "粥"]
elif 11 <= hour < 14:
    meal_type = "午餐"
    menu = ["米饭", "面条", "炒菜", "汤"]
elif 17 <= hour < 21:
    meal_type = "晚餐"
    menu = ["米饭", "炒菜", "汤", "水果"]
else:
    meal_type = "夜宵"
    menu = ["面条", "小菜", "饮料"]

print(f"当前是{meal_type}时间")
print(f"推荐菜单: {', '.join(menu)}")

print("\n" + "=" * 50)
print("🎉 if 条件判断练习完成！")
print("=" * 50) 