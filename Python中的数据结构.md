# 列表 List
`List`用`[ ]`表示，是Python中使用最频繁且最通用的复合数据类型。

**列表中的正反索引：**
![列表中的正反索引](https://raw.githubusercontent.com/liuzhen153/play-algorithm-python/master/images/list_suoyin.png)

## 特点
* 列表中每个元素都可变（修改、删除）
* 列表是有序的，可以用索引去访问指定元素
* 列表中的元素可以是`Python`中的任何对象，可以是字符串、整数、元组、也可以是list等Python中的对象
* 列表中值得切割可以用到变量`[头下标:尾下标]`，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾
* 加号 + 是列表连接运算符，星号 * 是重复操作

## 基础操作

```python
list = ['play', 'algorithm', 'python', 2019, 5.11, 'python']
author_list = ['Tommy', 'ChaoChao', 'Wsqstar']

# 正数操作
print('完整列表 list：' , list)
print('第二个元素 list[1]：' , list[1])
print('第二个到第四个元素 list[1:3]：' , list[1:3])
print('第三个到最后一个元素 list[2:]：' , list[2:])

# 倒数操作，此时截取不包含冒号右侧
print('倒数第二个元素 list[-2]：' , list[-2])
print('倒数最后三个元素 list[-3:]：' , list[-3:])
print('倒数第二个到第四个元素 list[-4:-1]：' , list[-4:-1])

# * + 操作
print('输出列表两次 author_list * 2：' , author_list * 2)
print('两个列表组合 list + author_list：' , list + author_list)

# 元素是否存在于列表中
print('python是否在列表中：', 'python' in list)

# 迭代
print('迭代输出author_list每一项：')
for item in author_list:
    print(item)
```


**输出结果**
```
完整列表 list： ['play', 'algorithm', 'python', 2019, 5.11, 'python']
第二个元素 list[1]： algorithm
第二个到第四个元素 list[1:3]： ['algorithm', 'python']
第三个到最后一个元素 list[2:]： ['python', 2019, 5.11, 'python']

倒数第二个元素 list[-2]： 5.11
倒数最后三个元素 list[-3:]： [2019, 5.11, 'python']
倒数第二个到第四个元素 list[-4:-1]： ['python', 2019, 5.11]

输出列表两次 author_list * 2： ['Tommy', 'ChaoChao', 'Wsqstar', 'Tommy', 'ChaoChao', 'Wsqstar']
两个列表组合 list + author_list： ['play', 'algorithm', 'python', 2019, 5.11, 'python', 'Tommy', 'ChaoChao', 'Wsqstar']

python是否在列表中： True

迭代输出author_list每一项：
Tommy
ChaoChao
Wsqstar
```

## 基础函数

```Python
list = ['play', 'algorithm', 'python', 2019, 5.11, 'python']
int_list = [12, 22, 30, 13, 24, 1, 10, 10.3, -1]

print('列表长度 len(list)：', len(list))

# max() 和 min() 函数只支持列表元素为int和float这种可以计算数值大小的类型
print('最大值 max(int_list)：', max(int_list))
print('最小值 min(int_list)：', min(int_list))
```

**输出结果**
```
列表长度 len(list)： 6
最大值 max(int_list)： 30
最小值 min(int_list)： -1
```


## 基础方法

```Python
list = ['play', 'algorithm', 'python', 2019, 5.11, 'python']
author_list = ['Tommy', 'ChaoChao', 'Wsqstar']

list.append(author_list)
print('在末尾添加新对象 list.append(author_list)：', list)

list.remove(author_list)
print("移除某个元素第一个匹配项 list.remove(author_list)：", list)

list.insert(5, 'Baidu')
print("在指定位置添加新对象 list.insert(5, 'Baidu')：", list)

list.extend(author_list)
print('批量添加另一个列表中的值到末尾 list.extend(author_list)：', list)

print("统计某个元素在列表中出现的次数 list.count('python')：", list.count('python'))

print("找出某个元素第一次出现的索引位置 list.index('python')：", list.index('python'))

list.pop()
print("移除一个元素，默认最后一个元素 list.pop()：", list)
list.pop(0)
# list.pop([index = -1])方法同del，以下例子也可以用del语句：del list[0]
print("移除第一个元素 list.pop(0)：", list)

list.reverse()
print("将列表元素反向 list.reverse()：", list)

print('列表排序，建议查看菜鸟教程获得更好的讲述：' , 'https://www.runoob.com/python/att-list-sort.html')

list2 = list.copy()
print("列表复制,我是list复制来的list2 list.copy()：", list2)

list2.clear()
print('list2清空后 list2.clear()：', list2)
# 复制和使用 = 赋值不同，复制产生了新的列表，对list2的任何操作不影响list
print('list2清空后的list：', list)

# 使用 = 赋值时，所有的操作都会影响到list本身
list3 = list
print('我是赋值来的list3：', list3)
list3.clear()
print('list3清空后 list3.clear()：', list3)
print('list3清空后的list：', list)
```

**输出结果**
```
在末尾添加新对象 list.append(author_list)： ['play', 'algorithm', 'python', 2019, 5.11, 'python', ['Tommy', 'ChaoChao', 'Wsqstar']]
移除某个元素第一个匹配项 list.remove(author_list)： ['play', 'algorithm', 'python', 2019, 5.11, 'python']

在指定位置添加新对象 list.insert(5, 'Baidu')： ['play', 'algorithm', 'python', 2019, 5.11, 'Baidu', 'python']
批量添加另一个列表中的值到末尾 list.extend(author_list)： ['play', 'algorithm', 'python', 2019, 5.11, 'Baidu', 'python', 'Tommy', 'ChaoChao', 'Wsqstar']

统计某个元素在列表中出现的次数 list.count('python')： 2
找出某个元素第一次出现的索引位置 list.index('python')： 2

移除一个元素，默认最后一个元素 list.pop()： ['play', 'algorithm', 'python', 2019, 5.11, 'Baidu', 'python', 'Tommy', 'ChaoChao']
移除第一个元素 list.pop(0)： ['algorithm', 'python', 2019, 5.11, 'Baidu', 'python', 'Tommy', 'ChaoChao']

将列表元素反向 list.reverse()： ['ChaoChao', 'Tommy', 'python', 'Baidu', 5.11, 2019, 'python', 'algorithm']
列表排序，建议查看菜鸟教程获得更好的讲述： https://www.runoob.com/python/att-list-sort.html

列表复制,我是list复制来的list2 list.copy()： ['ChaoChao', 'Tommy', 'python', 'Baidu', 5.11, 2019, 'python', 'algorithm']
list2清空后 list2.clear()： []
list2清空后的list： ['ChaoChao', 'Tommy', 'python', 'Baidu', 5.11, 2019, 'python', 'algorithm']

我是赋值来的list3： ['ChaoChao', 'Tommy', 'python', 'Baidu', 5.11, 2019, 'python', 'algorithm']
list3清空后 list3.clear()： []
list3清空后的list： []
```

# 元组 Tuple
`Tuple`用`( )`表示，可以理解为一个固定列表，一旦初始化就不能再修改，只能对元素进行查询。

## 特点
* 元素只读，不支持对元素进行添加、修改（删除）
* 代码更安全
* 内置大多数方法和`List`差不多

## 基础操作

```python
tuple1 = ('play', 'algorithm', 'python', 2019, 5.11, 'python')
# 空元组
empty_tup = ()
# 只有一个元素的元组，需要最后添加逗号，如果不加逗号，两边的括弧会被认为是数学公式中的小括号
one_item_tup = ('Tommy',)

print('元组示例：', tuple1)
print('空元组：', empty_tup)
print('只有一个元素的元组：', one_item_tup)

# 截取、*、判断元素是否存在、迭代等操作同列表
print('截取、*、判断元素是否存在、迭代等操作同列表')
print('两个元组组合，形成新元组 tuple1 + one_item_tup：' , tuple1 + one_item_tup)
```


**输出结果**
```
元组示例： ('play', 'algorithm', 'python', 2019, 5.11, 'python')
空元组： ()
只有一个元素的元组： ('Tommy',)

截取、*、判断元素是否存在、迭代等操作同列表

两个元组组合，形成新元组 tuple1 + one_item_tup： ('play', 'algorithm', 'python', 2019, 5.11, 'python', 'Tommy')
```

## 无关闭运算符
任何以逗号分隔的无符号对象，默认为元组
```python
m = 'play', 'algorithm', 'python', 18+6.6j, -4.24e93
x, y = 1, 2
print('m的值是：', m)
print('x, y的值是：', x, y)
```

**输出结果**
```
m的值是： ('play', 'algorithm', 'python', (18+6.6j), -4.24e+93)
x, y的值是： 1 2
```

## 基础函数

```Python
print('len(tuple) min(tuple) max(tuple)和列表用法相同')

```

**输出结果**
```

```


## 震惊，元组居然能改变？


# 字典 Dict
# 集合 Set
