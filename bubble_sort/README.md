# 冒泡排序

## 示意图
![冒泡排序示意图](https://raw.githubusercontent.com/liuzhen153/play-algorithm-python/master/images/bubble_sort.png)

## 运作步骤
1. 比较相邻的元素，如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

## 助记码
```
i∈[0,N-1)               //循环N-1遍
  j∈[0,N-1-i)           //每遍循环要处理的无序部分
    swap(j,j+1)          //两两排序（升序/降序）
```

## 算法分析
* 最坏时间复杂度	O(n^2)
* 最优时间复杂度	O(n)
* 平均时间复杂度	O(n^2)

## 实现
```Python
def bubble_sort(list=[]):
    '''Python中的冒泡排序算法实现
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    list_len = len(list)
    for i in range(list_len - 1):          # 剩一个元素时不需要再比较
        swap = 0                           # 记录是否
        for j in range(list_len - 1 - i):  # 每次都需要两两对比前面未排序完成的元素
            if list[j + 1] < list[j]:        # 比较相邻元素
                swap += 1
                list[j], list[j + 1] = list[j + 1], list[j]  # 根据大小调换元素位置
        if swap == 0:                      # 如果内循环没有大小交换，则代表已排序完成，不必再往下进行
            break
    return list
```

## 测试
```
$ python bubble_sort.py
冒泡排序>>>
请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：
需要排序的数字为：
8,-5,10,6,-23,15,45
排序结果：
-23,-5,6,8,10,15,45
```
