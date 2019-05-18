# 插入排序

## 示意图
![冒泡排序示意图](https://raw.githubusercontent.com/liuzhen153/play-algorithm-python/master/images/insertion_sort.gif)

## 运作步骤
1. 第一个元素可被认为已被排序。
2. 取出下一个元素，在已排序的元素序列中从后向前扫描。
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置。
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置。
5. 将新元素插入到该位置后。
6. 重复步骤2~5。

## 助记码
```
i∈[1,N)                 //循环N-1遍
  j∈[i, 0, -1)           //每遍循环已排序部分
    swap(j,j-1)          //将大值往后移
```

## 算法分析
* 最坏时间复杂度	O(n^2)
* 最优时间复杂度	O(n)
* 平均时间复杂度	O(n^2)

## 实现
```Python
def insertion_sort_1(list):
    '''Python中的插入排序算法实现1
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    list_len = len(list)
    for i in range(1, list_len):            # 第一个元素默认为已被排序
        for j in range(i, 0, -1):           # 将已被排序的序列从后向前扫描
            if list[j - 1] > list[j]:         # 如果该元素（已排序）大于新元素，将该元素移到下一位置
                list[j - 1], list[j] = list[j], list[j - 1]
            else:
                break
    return list


def insertion_sort_2(list):
    '''Python中的插入排序算法实现2
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    list_len = len(list)
    for i in range(1, list_len):            # 第一个元素默认为已被排序
        j = i - 1                           # 记录往前扫描的key
        while j >= 0 and list[i] < list[j]: # 如果已排序的序列从后往前扫描，发现当前比新元素大，则往后移一位
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = list[i]                # 新元素添加到找到的key后方，前是小，后是大
    return list


def insertion_sort_3(list):
    '''Python中的插入排序算法实现3
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    for i in range(1, len(list)):                       # 第一个元素默认为已被排序
        while i > 0 and list[i - 1] > list[i]:          # 将新元素和前方元素一一对比，若新元素比较小，则交换两者位置
            list[i], list[i - 1] = list[i - 1], list[i]
            i -= 1
    return list

```

## 测试
```
$ python insertion_sort.py
插入排序>>>
请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：
需要排序的数字为：
8,-5,10,6,-23,15,45
insertion_sort_1 排序结果：
-23,-5,6,8,10,15,45
insertion_sort_2 排序结果：
-23,-5,6,8,10,15,45
insertion_sort_3 排序结果：
-23,-5,6,8,10,15,45
```
