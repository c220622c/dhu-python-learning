# 期中复习

# 程序原理与概述

### 1. 程序的基本概念

- 计算机根据指令操作数据的设备
- 程序是能够完成特定功能的一组指令序列
- 程序的基本流程：输入数据 → 处理数据 → 输出数据

## Python 语法元素->`/cpython-main/Grammar/`

### 2.1 基础元素

- **常量**: 初始化后保持固定不变的值 (如：1, 3.14, 'Python', False),定义一个不变的变量就可以了，不像别的语言

```rust
let x = 5
let mut x =5
```

- **变量**: 程序中值发生改变或可以发生改变的元素
- **保留字/关键字**: Python 预定义的词汇，不能用作变量名,可以参考`cpython-main/Lib/keyword.py`

  ```python
  kwlist = [
    'False',
    'None',
    'True',
    'and',
    'as',
    'assert',
    'async',
    'await',
    'break',
    'class',
    'continue',
    'def',
    'del',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'if',
    'import',
    'in',
    'is',
    'lambda',
    'nonlocal',
    'not',
    'or',
    'pass',
    'raise',
    'return',
    'try',
    'while',
    'with',
    'yield'
  ]

  softkwlist = [
    '_',
    'case',
    'match',
    'type'
  ]
  ```

- **标识符命名规则**:
  - 首字符不能是数字，中间不能有空格，不能与保留字相同,大小写敏感
  - 变量与函数：清楚表达意思，比如 open_txt_data
  - 类名：驼峰命名法，`class DataProcessor`
  - 常量：全大写，`DEFAULT_TIMEOUT`
  - 私有成员：前缀下划线
  ```python
  class MyClass:
    def __init__(self):
        self._internal_var = "私有变量"
        self.__private_var = "更私有的变量"
  ```
  - 布尔值变量：以 is 开头`isPrime`
  - 复数变量，以 s 结尾

### 2.2 运算符

- **算术运算符**: `+`, `-`, `*`, `/`, `%` (取余), `**` (求幂), `//` (取整除)
- **赋值运算符**: `=`, `+=`, `-=`, `*=`, `/=`,
- **比较运算符**: `==`, `!=`, `>`, `>=`, `<`, `<=`
- **逻辑运算符**: `and` (与), `or` (或), `not` (非)
- **运算优先级**: `or < and < not`

### 2.3 表达式

- 包含多次多种运算的表达式
- 示例：`1+2`, `2*(x+y)`, `0<=a<=10`

### 2.4 内置函数

- **type()函数**: 返回变量类型
- **print()函数**: 控制台输出

  - 输出变量: `print(a)`
  - 输出字符串: `print("hello world")`
  - 格式化输出: `print("模板字符串".format(参数))`

  ```python
  print("{}{}".format("Hello, ", "world!"))
  ```

- **input()函数**: 控制台输入
  - 返回值默认为字符串类型
- **eval()函数**: 将字符串转换为数字或表达式
  - 常与 input()函数联用进行数值输入

### 2.5 format()方法详解

- **基本格式**: `"{参数序号:格式控制标记}"`
- **格式控制标记**:
  - `<填充><对齐><宽度>`: 控制显示宽度和对齐方式
  - `<.精度><类型>`: 控制小数位数和数据类型
- **示例**: `"{0:-^30}".format(s)` (宽度 30，居中对齐，'-'填充)
- **示例**: `"{:.2f}".format(s)` (保留两位小数)

```python
# 对齐和宽度
"{:<10}".format("left")      # "left      " (左对齐)
"{:>10}".format("right")     # "     right" (右对齐)
"{:^10}".format("center")    # "   center " (居中对齐)

# 数值格式化
"{:d}".format(42)           # "42" (十进制)
"{:x}".format(255)          # "ff" (十六进制)
"{:o}".format(8)            # "10" (八进制)

# 浮点数格式化
"{:.2f}".format(3.14159)    # "3.14" (2位小数)
"{:,.2f}".format(1234.5678) # "1,234.57" (千分位分隔)

# 百分比
"{:%}".format(0.1234)        # "12.340000%"
"{:.1%}".format(0.1234)      # "12.3%"

# 科学计数法
"{:e}".format(1234.56)       # "1.234560e+03"
"{:.2e}".format(1234.56)     # "1.23e+03"
now = datetime.now()
"{:%Y-%m-%d %H:%M:%S}".format(now)  # "2024-01-15 14:30:25"
"{:%B %d, %Y}".format(now)           # "January 15, 2024"
"{:%A, %B %d, %Y}".format(now)      # "Monday, January 15, 2024"
```

## 程序基本结构

### 3.1 三种基本结构

- **顺序结构**: 按顺序执行每条语句
- **分支结构**: 选择性地执行部分语句
- **循环结构**: 重复性地执行部分语句

### 3.2 分支结构

- **单分支**:

```python
if true:
  do sth
```

- **二分支**:

```python
if isPrime(n):
  print("isprime")
else:
  print("...")
```

- **多分支**:

```python
if n==2:
  print("isprime")
elif isPrime(n):
  print("isprime")
else:
  print("...")
```

### 3.3 循环结构

- **遍历循环 (for 循环)**:`for i in range(len(tupleA)):`

  - 遍历对象：字符串、文件、组合数据类型、range()函数

- **无限循环 (while 循环)**:

```python
while ifPrint(tupleA[i])
  print(tupleA[i])
  i = i + 1
```

- **循环控制**:
  - `break`: 中断当前循环
  - `continue`: 中断本次循环，进入下一轮

### 3.4 循环嵌套

- 解决复杂问题，嵌套层数不限
- 内外层之间不能交叉
- 双层循环：总次数等于内外层次数之积

## 第四部分：数据类型

### 4.1 基本数据类型

- **数字类型**:

  - 整数 (int): `1`
  - 浮点数 (float): `1.1`
  - 复数 (complex): `1 + 2j`
  - 布尔值 (bool): `True, False`

- **字符串 (string)**:
  - 单引号: `'hello world'`
  - 双引号: `"hello world"`
  - 三引号: `'''hello world'''`
  - 索引访问: 正向递增序号，反向递减序号

### 4.2 类型转换

- **转换函数**: `str()`, `int()`, `float()`, `complex()`, `bool()`
- **转换规则**:
  - `int(4.5) = 4` (直接去掉小数部分)
  - `str(-1.0) = '-1.0'` (保留小数部分)
  - `round(1.5) = 2` (四舍五入)

### 4.3 组合数据类型

#### 序列类型

- **元组 (tuple)**: 不可变序列 `bbb_tuple = (1,2,3,4)`
- **列表 (list)**: 可修改序列 `ccc_list = [1,2,3,4]`

#### 集合类型

- **集合 (set)**: 无序组合，元素不可重复 `ddd_set = {1,2,3}`

#### 映射类型

- **字典 (dict)**: 键值对映射 `eee_dict = {"key": "value"}`

### 4.4 组合数据类型操作

- **索引操作**: 元组 ✅, 列表 ✅, 集合 ❌, 字典 ❌
- **切片操作**: 元组 ✅, 列表 ✅, 集合 ❌, 字典 ❌
- **类型相加**: 元组 ✅, 列表 ✅, 集合 ❌, 字典 ❌
- **成员资格**: 全部类型支持 (`in`操作符)
- **长度函数**: 全部类型支持 (`len()`函数)
- **最大/最小值**: 全部可迭代类型支持 (`max()`, `min()`)

### 4.5 列表专有操作

- **修改**: `ls[i] = x`
- **添加**: `ls.append(x)`, `ls.insert(i,x)`, `ls.extend(L)`
- **删除**: `del ls[i]`, `ls.pop(i)`, `ls.remove(x)`
- **排序**: `ls.sort()`, `ls.sort(reverse=True)`, `sorted(ls)`
- **反转**: `ls.reverse()`

### 4.6 字典专有操作

- **创建**: `d = {}` 或 `d = {key1: value1, key2: value2}`
- **添加/修改**: `d[key] = value`
- **访问**:
  - 索引方式: `d[key]` (键不存在时报错)
  - get 方式: `d.get(key, default)` (键不存在返回默认值)
- **删除**: `del d[key]`, `d.pop(key)`, `d.popitem()`, `d.clear()`
- **遍历**:
  - 遍历键值对: `for k, v in d.items():`
  - 遍历键: `for k in d.keys():` 或 `for k in d:`
  - 遍历值: `for v in d.values():`
  - 按序遍历键: `for k in sorted(d.keys()):`

## 第五部分：实际应用案例

### 5.1 字符串格式化应用

- 日志输出格式化
- 多变量同时输出
- 数值精度控制

### 5.2 统计应用

- 成绩分布统计
- 频次计算
- 字典统计应用

### 5.3 通讯录管理

- 添加联系人
- 删除联系人
- 查找联系人
- 显示电话本

## 学习要点总结

1. **掌握基础语法**: 熟悉 Python 的标识符、关键字、运算符等基本元素
2. **理解程序结构**: 掌握顺序、分支、循环三种基本结构的使用
3. **熟练数据类型**: 重点掌握字符串、列表、字典等常用数据类型的操作
4. **掌握函数使用**: 熟练使用 print、input、format 等内置函数
5. **实践编程能力**: 通过实际案例练习综合运用所学知识
