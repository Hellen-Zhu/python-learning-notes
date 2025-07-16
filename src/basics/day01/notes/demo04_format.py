name = 'Hellen'
sex = 'Female'
age = 36

print(f"My name is {name}, I am a {sex}, my age is {age}")

# 转义符， \n是换行
print(f"My name is {name}, \nI am a {sex}, \nmy age is {age}")
print(f"My name is {name}, \tI am a {sex}, \tmy age is {age}")

num1 = int(input("Input number1:"))
num2 = int(input("Input number2:"))

result = num1+num2

print(f'{num1}+{num2}={result}')

name = input("请输入姓名:")
age = int(input("请输入年龄:"))
height = float(input("I请输入身高:"))
is_adult=False
print(type(name), type(age),type(height))

print(f"姓名:{name} 年龄:{age} 身高:{height}")

new_age = age+5
print(f"{name} 5 年之后的年龄是 {new_age}")

if(age>=18):
    is_adult=True
    print(f'{name}是否成年:{is_adult}')

# 1. 提示用户输入用户姓名，并保存到变量中
name = input('请输入姓名:')

# 2. 提示用户输入用户年龄，保存到变量中，并转换成整数
age = int(input('请输入年龄:'))

# 3. 提示用户输入用户身高，保存到变量中，并转换成浮点数
height = float(input('请输入身高:'))

# 4. 在控制台输出用户姓名、年龄、身高对应变量的数据类型
print(type(name), type(age), type(height))

# 5. 按照以下格式输出用户信息:“姓名:xxx 年龄:xxx 身高:xxx”
print(f"姓名:{name} 年龄:{age} 身高:{height}")

# 6. 在控制台输出该用户5年之后的年龄，格式:“张三 5 年之后的年龄是 25”
age = age + 5
print(f"{name} 5 年之后的年龄是 {age}")

# 7. 在控制台输出该用户现在是否成年，格式:“张三是否成年:True”
print(f"{name}是否成年:{age >= 18}")