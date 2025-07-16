# Python Learning Notes

## 项目简介
这是我的Python自学笔记和练习项目集合。通过这个项目记录学习过程，分享学习心得，帮助其他Python初学者。

## 学习内容
- Python基础语法
- 数据类型和数据结构
- 运算符和条件判断
- 循环控制结构
- 函数和面向对象编程
- 实际项目练习

## 项目结构
```
python-learning-notes/
├── README.md                 # 项目说明
├── requirements.txt          # 依赖文件
├── src/                     # 源代码目录
│   ├── basics/             # 基础语法
│   │   ├── day01/          # 第一天学习内容
│   │   │   ├── notes/      # 学习笔记
│   │   │   │   ├── demo01_comment.py      # 注释方式详解
│   │   │   │   ├── demo02_naming_convention.py  # 变量命名规则
│   │   │   │   ├── demo03_data_type.py    # 数据类型详解
│   │   │   │   ├── demo04_format.py       # 字符串格式化
│   │   │   │   ├── demo05_operator.py     # 运算符详解
│   │   │   │   ├── demo06_if.py           # 条件判断详解
│   │   │   │   └── demo07_for.py          # for循环详解
│   │   │   └── homework/   # 作业练习
│   │   │       ├── calculator.py          # 计算器程序
│   │   │       ├── guess_num.py           # 猜数字游戏
│   │   │       └── operators.py           # 运算符练习
│   │   └── day02/          # 第二天学习内容
│   ├── functions/          # 函数
│   ├── oop/               # 面向对象
│   └── projects/          # 小项目
├── docs/                  # 文档
│   └── learning_notes.md  # 学习笔记
└── tests/                 # 测试
```

## 学习进度
- [x] 变量和数据类型
- [x] 列表、元组、集合、字典
- [x] 注释方式
- [x] 命名规则
- [x] 类型转换
- [x] 运算符详解
- [x] 条件判断 (if语句)
- [x] 循环控制 (for循环)
- [ ] 函数定义和使用
- [ ] 面向对象编程
- [ ] 文件操作
- [ ] 异常处理

## 文件说明

### 第一天学习笔记 (src/basics/day01/notes/)
- `demo01_comment.py` - Python注释方式详解，包括单行注释、多行注释、文档字符串等
- `demo02_naming_convention.py` - Python命名规则详解，包括变量、函数、类、文件命名规范
- `demo03_data_type.py` - Python数据类型详解，包括数字、字符串、列表、元组、集合、字典的对比和使用
- `demo04_format.py` - 字符串格式化详解，包括f-string、format()方法、%操作符等
- `demo05_operator.py` - 运算符详解，包括算术、比较、逻辑、赋值、位运算、成员、身份运算符等
- `demo06_if.py` - 条件判断详解，包括单分支、双分支、多分支、嵌套条件、三元运算符等
- `demo07_for.py` - for循环详解，包括基本遍历、range()使用、嵌套循环、条件控制、列表推导式等

### 第一天作业练习 (src/basics/day01/homework/)
- `calculator.py` - 简单计算器程序，实现四则运算
- `guess_num.py` - 猜数字游戏，练习循环和条件判断
- `operators.py` - 运算符练习，巩固各种运算符的使用

## 学习心得

### 基础语法掌握
1. **注释的重要性** - 良好的注释习惯让代码更易读和维护
2. **命名规范** - 遵循PEP 8命名规范，提高代码可读性
3. **数据类型** - 理解不同数据类型的特性和使用场景
4. **字符串格式化** - 掌握f-string、format()方法等格式化技巧

### 运算符理解
1. **算术运算符** - 基本的数学运算，包括整除和取模
2. **比较运算符** - 用于条件判断的比较操作
3. **逻辑运算符** - and、or、not的组合使用
4. **赋值运算符** - 简化代码的复合赋值操作
5. **位运算符** - 底层位操作，用于权限控制等场景
6. **成员运算符** - in、not in用于检查元素是否在序列中
7. **身份运算符** - is、is not用于对象身份比较

### 条件判断掌握
1. **if-elif-else结构** - 多分支条件判断
2. **嵌套条件** - 复杂逻辑的条件组合
3. **三元运算符** - 简洁的条件表达式
4. **特殊条件判断** - 空值、零值、空集合的判断

### 循环控制理解
1. **for循环基础** - 遍历各种数据类型
2. **range()函数** - 生成数字序列
3. **enumerate()** - 带索引的遍历
4. **嵌套循环** - 处理二维数据结构
5. **循环控制** - break、continue、else子句
6. **列表推导式** - 简洁的列表生成方式
7. **高级技巧** - zip()、filter()、map()等函数式编程

### 字符串格式化掌握
1. **f-string** - Python 3.6+的现代格式化方式，简洁高效
2. **format()方法** - 灵活的格式化选项，支持位置和关键字参数
3. **%操作符** - 传统的格式化方式，兼容性好
4. **转义字符** - 掌握常用的转义字符和格式化技巧

## 实际应用场景

### 计算器程序
实现了简单的四则运算计算器，包含：
- 用户输入处理
- 运算符判断
- 错误处理（除零检查）
- 格式化输出

### 数据处理
- 学生成绩分析
- 文本处理和分析
- 购物车系统
- 库存管理

## 如何运行

### 环境配置
```bash
# 克隆项目
git clone https://github.com/Hellen-Zhu/python-learning-notes.git

# 进入项目目录
cd python-learning-notes

# 创建虚拟环境
python3.12 -m venv .venv

# 激活虚拟环境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 运行示例
```bash
# 第一天学习笔记示例
python src/basics/day01/notes/demo01_comment.py
python src/basics/day01/notes/demo02_naming_convention.py
python src/basics/day01/notes/demo03_data_type.py
python src/basics/day01/notes/demo04_format.py
python src/basics/day01/notes/demo05_operator.py
python src/basics/day01/notes/demo06_if.py
python src/basics/day01/notes/demo07_for.py

# 第一天作业练习
python src/basics/day01/homework/calculator.py
python src/basics/day01/homework/guess_num.py
python src/basics/day01/homework/operators.py
```

## 学习资源
- [Python官方文档](https://docs.python.org/3/)
- [PEP 8 风格指南](https://www.python.org/dev/peps/pep-0008/)
- [Python教程](https://docs.python.org/3/tutorial/)

## 常见问题解决

### PyCharm调试器问题
如果遇到调试器连接失败，可能是文件名与Python标准库冲突：
- 避免使用 `operator.py`、`string.py` 等与标准库同名的文件名
- 清理Python缓存文件
- 重启PyCharm

### 虚拟环境配置
确保使用正确的Python版本和虚拟环境：
```bash
python --version  # 检查Python版本
which python      # 检查Python路径
```

## 贡献
欢迎提出建议和改进意见！如果你也是Python学习者，欢迎一起交流学习心得。

### 贡献方式
1. Fork 本项目
2. 创建新的分支
3. 提交你的更改
4. 创建 Pull Request

## 联系方式
- GitHub: [Hellen-Zhu](https://github.com/Hellen-Zhu)
- Email: 774804075@qq.com

---
*这是一个持续更新的学习项目，我会随着学习的深入不断添加新的内容和示例。* 