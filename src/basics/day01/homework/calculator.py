
'''
请输出第一个数字:
请输入第二个数字:
请输入要进行的操作(+ - * /):
计算的结果为:
举例如下:
请输出第一个数字: 10
请输入第二个数字: 20
请输入要进行的操作(+ - * /): +
计算的结果为: 10 + 20 = 30
```
'''

print("简单计算器")
print("=" * 30)

# 获取用户输入
num1 = float(input("请输出第一个数字: "))
num2 = float(input("请输入第二个数字: "))
operation = input("请输入要进行的操作(+ - * /): ")

result=0
# 根据操作符进行计算
if operation == "+":
    result = num1 + num2
    print(f"计算的结果为: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"计算的结果为: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"计算的结果为: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:  # 检查除数不为0
        result = num1 / num2
        print(f"计算的结果为: {num1} / {num2} = {result}")
    else:
        print("错误: 除数不能为0")

else:
    print("错误：不支持的操作符，请使用 +、-、*、/ 之一")

print("=" * 30)

