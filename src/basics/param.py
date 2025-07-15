# 变量需要先定义才能使用
age = 18
height= 170.1
sex = 'female'
print(age, height, sex)

# 命名规范 要符合标识符命名规则
"""
由字母，数字和下划线组成，但是不能以数字开头
"""

# Python 命名规则详解
"""
1. 标识符命名规则:
   - 只能包含字母、数字和下划线
   - 不能以数字开头
   - 区分大小写
   - 不能使用 Python 关键字作为标识符

2. 变量命名规范:
   - 使用小写字母和下划线(snake_case)
   - 例如:user_name, age, height_cm
   - 避免使用单字母变量名(除了循环变量 i, j, k)

3. 常量命名规范:
   - 使用大写字母和下划线
   - 例如:MAX_VALUE, PI, API_KEY

4. 函数命名规范:
   - 使用小写字母和下划线(snake_case)
   - 动词开头，描述函数功能
   - 例如:get_user_info(), calculate_area()

5. 类命名规范:
   - 使用大驼峰命名法(PascalCase)
   - 每个单词首字母大写
   - 例如:UserInfo, StudentClass

6. 模块和包命名规范:
   - 使用小写字母和下划线
   - 例如:user_management, data_processor

7. 私有变量和方法:
   - 单下划线开头表示内部使用(_private_var)
   - 双下划线开头表示私有(__private_var)

8. 特殊方法(魔术方法):
   - 双下划线开头和结尾
   - 例如:__init__, __str__, __len__

9. 避免的命名:
   - 不要使用拼音
   - 不要使用过于简单的名称
   - 不要使用有歧义的缩写
   - 避免使用 l(小写L)和 O(大写O)作为变量名

10. 推荐的命名长度:
    - 变量名:1-20个字符
    - 函数名:3-30个字符
    - 类名:3-40个字符
"""

# 驼峰命名法详解
"""
驼峰命名法分为两种:大驼峰(PascalCase)和小驼峰(camelCase)

1. 大驼峰命名法(PascalCase):
   格式:每个单词的首字母都大写
   使用场景:
   - 类名:UserInfo, StudentClass, DatabaseConnection
   - 异常类:ValueError, TypeError, CustomException
   - 枚举类:ColorEnum, StatusEnum
   - 接口类:UserInterface, DataProcessor
   - 抽象类:AbstractUser, BaseHandler
   
   示例:
   class UserManager:
   class DatabaseConnection:
   class CustomException(Exception):

2. 小驼峰命名法(camelCase):
   格式:第一个单词首字母小写，后续单词首字母大写
   使用场景:
   - JavaScript/Java 中的变量名和函数名
   - Python 中通常不使用，但了解有助于跨语言开发
   - 某些框架或库的 API 可能使用
   
   示例:
   userName = "张三"
   getUserInfo()
   calculateTotalPrice()

3. Python 中的实际应用:
   - Python 官方推荐使用 snake_case 而不是驼峰命名法
   - 只有类名使用大驼峰命名法
   - 变量、函数、方法都使用 snake_case
   
   正确示例:
   class UserManager:          # 大驼峰 - 类名
       def get_user_info(self): # snake_case - 方法名
           user_name = "张三"    # snake_case - 变量名
           return user_name

4. 为什么 Python 不使用小驼峰:
   - Python 的设计哲学强调可读性
   - snake_case 在视觉上更容易区分单词
   - 符合 PEP 8 官方风格指南
   - 与其他语言区分，形成 Python 特色

5. 跨语言开发注意事项:
   - JavaScript: 变量和函数用小驼峰，类用大驼峰
   - Java: 变量和方法用小驼峰，类用大驼峰
   - C#: 变量和方法用小驼峰，类用大驼峰
   - Python: 只有类用大驼峰，其他都用 snake_case
"""

# 大小写使用规则总结
"""
Python 中大小写字母的使用规则:

1. 使用大写字母的场景:
   - 类名:UserInfo, StudentClass, DatabaseConnection
   - 异常类:ValueError, TypeError, CustomException
   - 枚举类:ColorEnum, StatusEnum
   - 常量:MAX_VALUE, PI, API_KEY, DEFAULT_TIMEOUT
   - 模块级常量:CONFIG_FILE_PATH, LOG_LEVEL
   - 全局配置:DEBUG_MODE, PRODUCTION_ENV

2. 使用小写字母的场景:
   - 变量名:user_name, age, height_cm, is_valid
   - 函数名:get_user_info(), calculate_area(), validate_input()
   - 方法名:save_data(), update_record(), delete_item()
   - 模块名:user_management, data_processor, utils
   - 包名:my_package, test_utils, config
   - 文件名:main.py, user_model.py, database.py

3. 混合大小写的场景:
   - 类名:每个单词首字母大写 (PascalCase)
     * UserManager, DatabaseConnection, ApiClient
   - 常量:所有字母大写，单词间用下划线分隔
     * MAX_RETRY_COUNT, DEFAULT_TIMEOUT_SECONDS
   - 变量/函数:全小写，单词间用下划线分隔 (snake_case)
     * user_name, get_user_info(), calculate_total_price()

4. 特殊情况:
   - 私有变量/方法:单下划线开头，其余小写
     * _private_var, _internal_method()
   - 私有变量/方法:双下划线开头，其余小写
     * __private_var, __internal_method()
   - 魔术方法:双下划线开头和结尾，全小写
     * __init__, __str__, __len__, __getitem__

5. 命名长度建议:
   - 短名称(1-3字符):用于循环变量 i, j, k
   - 中等名称(4-15字符):变量、函数、方法
   - 长名称(16-40字符):类名、复杂概念
   - 避免过长名称(>40字符):影响可读性

6. 实际应用示例:
   # 常量 - 全大写
   MAX_CONNECTIONS = 100
   DEFAULT_TIMEOUT = 30
   
   # 类名 - 大驼峰
   class UserManager:
       # 方法名 - 小写+下划线
       def get_user_info(self):
           # 变量名 - 小写+下划线
           user_name = "张三"
           is_active = True
           return user_name
   
   # 函数名 - 小写+下划线
   def calculate_total_price(items):
       total = 0
       for item in items:
           total += item.price
       return total
"""
