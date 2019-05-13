def selection_sort(list):
    '''Python中的选择排序算法实现
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    list_len = len(list)
    for i in range(list_len):           # 需要对比n - 1次
        min_index = i                   # 假设当前位置是最小元素位置，min_index = i
        for j in range(i + 1, list_len):  # 遍历后面的元素
            if list[i] > list[j]:       # 如果后面元素有比当前位置小的值，则将min_index更新为这个元素的位置
                min_index = j
        if not min_index == i:          # 如果发现最小元素的键不是i，则将他们两个的值交换
            list[i], list[min_index] = list[min_index], list[i]
    return list


if __name__ == '__main__':
    print('选择排序>>>')
    user_input = input('请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：')
    example_list = 8, -5, 10, 6, -23, 15, 45
    unsorted_list = list(example_list) if user_input.strip() == '' else [
        int(item) for item in user_input.split(',')]
    print('需要排序的数字为：')
    print(*unsorted_list, sep=',')
    print('排序结果：')
    print(*selection_sort(unsorted_list), sep=',')
