def quick_sort(list):
    '''Python中的快速排序算法简单实现
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    if len(list) <= 1:
        return list
    less, greater, pivot = [], [], list.pop()
    for item in list:
        if item < pivot:
            less.append(item)
        else:
            greater.append(item)
    list.append(pivot)
    return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort_in_place(list):
    '''Python中的快速排序算法原地排序版本实现
    :param list: 需要排序的数字列表
    :return: 排序结果
    '''
    def partition(list, start, end):
        pivot = list[end]
        for j in range(start, end):
            if list[j] < pivot:
                list[start], list[j] = list[j], list[start]
                start += 1
        list[start], list[end] = list[end], list[start]
        return start

    def sort(list, start, end):
        if start >= end:
            return
        p = partition(list, start, end)
        sort(list, start, p - 1)
        sort(list, p + 1, end)

    sort(list, 0, len(list) - 1)
    return list


if __name__ == '__main__':
    print('快速排序>>>')
    user_input = input('请输入需要排序的数字，用英文半角逗号隔开，直接回车则使用默认数据：')
    example_list = 8, -5, 10, 6, -23, 15, 45, 20, 16
    unsorted_list = list(example_list) if user_input.strip() == '' else [
        int(item) for item in user_input.split(',')]
    print('需要排序的数字为：')
    print(*unsorted_list, sep=',')
    print('quick_sort排序结果：')
    print(*quick_sort(unsorted_list), sep=',')
    print('quick_sort_in_place排序结果：')
    print(*quick_sort_in_place(unsorted_list), sep=',')
