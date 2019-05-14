# 归并排序

## 示意图
![冒泡排序示意图](https://raw.githubusercontent.com/liuzhen153/play-algorithm-python/master/images/merge_sort.gif)

## 运作步骤
### 递归法（Top-down）

1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
4. 重复步骤3直到某一指针到达序列尾
5. 将另一序列剩下的所有元素直接复制到合并序列尾

### 迭代法（Bottom-up）
原理如下（假设序列共有n个元素）：

1. 将序列每相邻两个数字进行归并操作，形成 `ceil(n/2)`个序列，排序后每个序列包含两/一个元素
2. 若此时序列数不是1个则将上述序列再次归并，形成 `ceil(n/4)`个序列，每个序列包含四/三个元素
3. 重复步骤2，直到所有元素排序完毕，即序列数为1



## 算法分析
* 最坏时间复杂度	O(nlogn)
* 最优时间复杂度	O(nlogn)
* 平均时间复杂度	O(nlogn)

## 实现
```Python
def merge_sort(list):
    '''Python中的普通的归并排序算法实现
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    # 将left 和 right 按照大小排序
    def merge(left, right):
        '''merge两个list
        :param left: 列表left
        :param right: 列表right
        :return: merge结果
        '''
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        return result + left + right
    if len(list) <= 1:
        return list  # 只有一个元素时直接返回
    mid = len(list) // 2
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))


def merge_sort_fast(list):
    '''Python中的更快的归并排序算法实现
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    left, right = [], []
    while len(list) > 1:
        min_one, max_one = min(list), max(list)
        left.append(min_one)
        right.append(max_one)
        list.remove(min_one)
        list.remove(max_one)
    right.reverse()
    return left + list + right
```

## 测试
```
$ python merge_sort.py
归并排序>>>
请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：
需要排序的数字为：
1,4,2,3.6,-1,0,25,-34,8,9,1,0
merge_sort结果为：
-34,-1,0,0,1,1,2,3.6,4,8,9,25
运行一万次，merge_sort耗时： 0.2273240089416504
merge_sort_fast结果为：
-34,-1,0,0,1,1,2,3.6,4,8,9,25
运行一万次，merge_sort_fast耗时： 0.07656192779541016
此例子中，merge_sort_fast的效率是merge_sort的倍数： 2.0
```
