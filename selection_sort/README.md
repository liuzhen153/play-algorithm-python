# 选择排序

## 示意图
![冒泡排序示意图](https://raw.githubusercontent.com/liuzhen153/play-algorithm-python/master/images/selection_sort.gif)

## 运作步骤
1. 从第一个元素开始寻找最小（大）元素，存放在首位
2. 从剩余未排序的元素中继续寻找最小（大）元素，放到已排序的序列末尾
3. 重复上面的步骤直到最后一个元素

## 助记码
```
i∈[0,N)                 //循环N遍
  j∈[i,N-1)             //每遍循环要处理的无序部分
    swap(i,min_index)   //将最小（大）值和起始位置交换
```

## 算法分析
* 最坏时间复杂度	O(n^2)
* 最优时间复杂度	O(n^2)
* 平均时间复杂度	O(n^2)

## 实现
```Python
def selection_sort(list):
    '''Python中的选择排序算法实现
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    list_len = len(list)
    for i in range(list_len):
        min_index = i                   # 假设当前位置是最小元素位置，min_index = i
        for j in range(i+1, list_len):  # 遍历后面的元素
            if list[i] > list[j]:       # 如果后面元素有比当前位置小的值，则将min_index更新为这个元素的位置
                min_index = j
        if not min_index == i:          # 如果发现最小元素的键不是i，则将他们两个的值交换
            list[i], list[min_index] = list[min_index], list[i]
    return list
```

## 测试
```
$ python selection_sort.py
选择排序>>>
请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：
需要排序的数字为：
8,-5,10,6,-23,15,45
排序结果：
-23,-5,6,8,10,15,45
```
