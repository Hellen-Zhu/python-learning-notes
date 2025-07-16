# ===========================================
# Python 字典定义
# ===========================================

print("=" * 50)
print("Python 字典定义")
print("=" * 50)

# ===========================================
# 1. 字典定义
# ===========================================
# 使用类实例化的方式
dict1 = dict()
print(dict1)

dict2 = dict(name='张三',age=18)
print(dict2)

# 直接使用{}进行定义
dict3 = {'name':'张三','age':18}
print(dict3)

dict3['name']='Hellen'
print(dict3)

# dict3.pop('name')
# print(dict3)

print(dict3.get('age'))

for key in dict3:
    print(key)
for key in dict3.keys():
    print(key)
for value in dict3.values():
    print(value)

for key,value in dict3.items():
    print(key,value)

