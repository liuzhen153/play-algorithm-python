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


def main(list):
    import time
    start_time = time.time()

    for i in range(10000):
        merge_sort_result = merge_sort(list)

    print('merge_sort结果为：')
    print(*merge_sort_result, sep=',')
    merge_sort_end_time = time.time()
    merge_sort_time = merge_sort_end_time - start_time
    print('运行一万次，merge_sort耗时：', merge_sort_time)

    for i in range(10000):
        list_fast = list.copy()
        merge_sort_fast_result = merge_sort_fast(list_fast)

    print('merge_sort_fast结果为：')
    print(*merge_sort_fast_result, sep=',')
    merge_sort_fast_time = time.time() - merge_sort_end_time
    print('运行一万次，merge_sort_fast耗时：', merge_sort_fast_time)

    print('此例子中，merge_sort_fast的效率是merge_sort的倍数：',
          merge_sort_time // merge_sort_fast_time)


if __name__ == '__main__':
    print('归并排序>>>')
    user_input = input('请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：')
    example_list = 1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0
    unsorted_list = list(example_list) if user_input.strip() == '' else [
        int(item) for item in user_input.split(',')]
    print('需要排序的数字为：')
    print(*unsorted_list, sep=',')
    main(unsorted_list)
