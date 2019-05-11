# 列表 List
`List`用`[ ]`表示，是Python中使用最频繁且最通用的复合数据类型。
## 特点
* 列表中每个元素都可变（修改、删除）
* 列表是有序的，可以用索引去访问指定元素
* 列表中的元素可以是`Python`中的任何对象，可以是字符串、整数、元组、也可以是list等Python中的对象
* 列表中值得切割可以用到变量`[头下标:尾下标]`，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾
* 加号 + 是列表连接运算符，星号 * 是重复操作

**实例**
```
list = ['play', 'algorithm', 'python', 2019, 5.11]
author_list = ['Tommy', 'ChaoChao', 'Wsqstar']

print('输出完整列表：' , list)
print('输出第二个元素：' , list[1])
print('输出第二个到第四个元素：' , list[1:3])
print('输出第三个到最后一个元素：' , list[2:])
print('输出列表两次：' , author_list * 2)
print('输出两个列表组合：' , list + author_list)
```

**输出结果**
```
输出完整列表： ['play', 'algorithm', 'python', 2019, 5.11]
输出第二个元素： algorithm
输出第二个到第四个元素： ['algorithm', 'python']
输出第三个到最后一个元素： ['python', 2019, 5.11]
输出列表两次： ['Tommy', 'ChaoChao', 'Wsqstar', 'Tommy', 'ChaoChao', 'Wsqstar']
输出两个列表组合： ['play', 'algorithm', 'python', 2019, 5.11, 'Tommy', 'ChaoChao', 'Wsqstar']
```

# 元组 Tuple
# 字典 Dict
# 集合 Set
