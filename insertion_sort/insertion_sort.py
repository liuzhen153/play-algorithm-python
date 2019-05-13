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
        while j >= 0 and list[i] < list[j]:  # 如果已排序的序列从后往前扫描，发现当前比新元素大，则往后移一位
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
        # 将新元素和前方元素一一对比，若新元素比较小，则交换两者位置
        while i > 0 and list[i - 1] > list[i]:
            list[i], list[i - 1] = list[i - 1], list[i]
            i -= 1
    return list


if __name__ == '__main__':
    print('插入排序>>>')
    user_input = input('请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：')
    example_list = 8, -5, 10, 6, -23, 15, 45
    unsorted_list = list(example_list) if user_input.strip() == '' else [
        int(item) for item in user_input.split(',')]
    print('需要排序的数字为：')
    print(*unsorted_list, sep=',')
    print('insertion_sort_1 排序结果：')
    print(*insertion_sort_1(unsorted_list), sep=',')
    print('insertion_sort_2 排序结果：')
    print(*insertion_sort_2(unsorted_list), sep=',')
    print('insertion_sort_3 排序结果：')
    print(*insertion_sort_3(unsorted_list), sep=',')
