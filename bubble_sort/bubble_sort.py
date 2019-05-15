def bubble_sort(list=[]):
    '''Python中的冒泡排序算法实现
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    list_len = len(list)
    for i in range(list_len - 1):            # 剩一个元素时不需要再比较
        swap = False                         # 记录是否
        for j in range(list_len - 1 - i):    # 每次都需要两两对比前面未排序完成的元素
            if list[j + 1] < list[j]:        # 比较相邻元素
                list[j], list[j + 1], swap = list[j + 1], list[j], True  # 根据大小调换元素位置
        if not swap: break                   # 如果内循环没有大小交换，则代表已排序完成，不必再往下进行

    return list


if __name__ == '__main__':
    print('冒泡排序>>>')
    user_input = input('请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：')
    example_list = 8, -5, 10, 6, -23, 15, 45
    unsorted_list = list(example_list) if user_input.strip() == '' else [
        int(item) for item in user_input.split(',')]
    print('需要排序的数字为：')
    print(*unsorted_list, sep=',')
    print('排序结果：')
    print(*bubble_sort(unsorted_list), sep=',')
