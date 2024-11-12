#冒泡排序—交换类排序
def bubble_Sort1(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr

#print(bubble_Sort1([1,3,4,5,2,7,9]))

def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = True  # 标记
        for j in range(1, n - i):
            if ary[j] < ary[j - 1]:
                ary[j], ary[j - 1] = ary[j - 1], ary[j]
                flag = False
        # 某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了
        if flag:
            break
    return ary

def bubble_sort3(ary):
    n = len(ary)
    k = n  # k为循环的范围，初始值n
    for i in range(n):
        flag = True
        for j in range(1, k):  # 只遍历到最后交换的位置即可
            if ary[j - 1] > ary[j]:
                ary[j - 1], ary[j] = ary[j], ary[j - 1]
                k = j  # 记录最后交换的位置
                flag = False
        if flag:
            break
    return ary


#快速排序—交换类排序
def quick_sort1(ary):
    return qsort(ary, 0, len(ary) - 1)
def qsort(ary, start, end):
    if start < end:
        left = start
        right = end
        key = ary[start]
    else:
        return ary
    while left < right:
        while left < right and ary[right] > key:
            right -= 1
        if left < right:  # 说明打破while循环的原因是ary[right] <= key
            ary[left] = ary[right]
            left += 1
        while left < right and ary[left] < key:
            left += 1
        if left < right:  # 说明打破while循环的原因是ary[left] >= key
            ary[right] = ary[left]
            right -= 1
    ary[left] = key  # 此时，left=right，用key来填坑
    qsort(ary, start, left - 1)
    qsort(ary, left + 1, end)
    return ary

# 利用栈实现快排
def quicksort2(nums):
    if len(nums) <= 1:
        return nums
    # 左子数组
    less = []
    # 右子数组
    greater = []
    # 基准数
    base = nums.pop()
    # 对原数组进行划分
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)
    # 递归调用
    return quicksort2(less) + [base] + quicksort2(greater)
#print(quicksort2([1,3,4,5,2,7,9]))


#选择排序—选择类排序
# 每次找到最小元素，存放到起始位置
def selectionSort(arr):
    for i in range(len(arr) - 1):  # 最小的，次小的…
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


#堆排序—选择类排序
# 构建最大堆，移除根节点，重建堆
def heap_sort(ary):
    n = len(ary)
    first = int(n / 2 - 1)  # 最后一个非叶子节点
    for start in range(first, -1, -1):
        max_heapify(ary, start, n - 1)  # 构建最大堆
    for end in range(n - 1, 0, -1):  # 堆排，将最大跟堆转换成有序数组
        ary[end], ary[0] = ary[0], ary[end]  # 将根节点元素与最后叶子节点进行互换，取出最大根节点元素，对剩余节点重新构建最大堆
        max_heapify(ary, 0, end - 1)
    return ary


# start为当前需要调整最大堆的位置（最后一个父节点），end为调整边界
def max_heapify(ary, start, end):
    root = start
    while True:
        child = root * 2 + 1  # 调整节点的子节点
        if child > end:
            break
        if child + 1 <= end and ary[child] < ary[child + 1]:
            child = child + 1  # 取较大的子节点
        if ary[root] < ary[child]:  # 较大的子节点成为父节点
            ary[root], ary[child] = ary[child], ary[root]  # 交换
            root = child
        else:
            break

#插入排序—插入类排序
# 对于未排序数组，在已排序列从后向前扫描，找到相应位置再插入
def insert_sort(ary):
    count = len(ary)
    for i in range(1, count):
        j = i
        mark = ary[i]  # 注： 必须将ary[i]赋值为mark，不能直接用ary[i]
        while j - 1 >= 0 and ary[j - 1] > mark:
            ary[j] = ary[j - 1]
            j -= 1
        ary[j] = mark
    return ary


#希尔排序—插入类排序
# 分组插入排序，缩小增量排序，使用gap
def shell_sort(ary):
    count = len(ary)
    gap = round(count / 2)
    # 双杠用于整除（向下取整），在python直接用 “/” 得到的永远是浮点数，
    # 用round()得到四舍五入值
    while gap >= 1:
        for i in range(gap, count):
            temp = ary[i]
            j = i
            while j - gap >= 0 and ary[j - gap] > temp:  # 这里与插入排序一样
                ary[j] = ary[j - gap]
                j -= gap
            ary[j] = temp
        gap = round(gap / 2)
    return ary


#归并排序
# 分治法，待排序序列分成若干子序列，子序列有序，再把子序列合并为整体有序序列
def merge_sort(ary):
    if len(ary) <= 1:
        return ary
    median = int(len(ary) / 2)  # 二分分解
    left = merge_sort(ary[:median])
    right = merge_sort(ary[median:])
    return merge(left, right)  # 合并数组

def merge(left, right):
    '''合并操作将两个有序数组left[]和right[]合并成一个大的有序数组'''
    res = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res = res + left[i:] + right[j:]
    return res


#基数排序
# 从最低位到最高位排序完成
def RadixSort(input_list):
    def MaxBit(input_list):
        max_data = max(input_list)
        bits_num = 0
        while max_data:
            bits_num += 1
            max_data //= 10
        return bits_num

    def digit(num, d):
        p = 1
        while d > 1:
            d -= 1
            p *= 10
        return num // p % 10

    if len(input_list) == 0:
        return []
    sorted_list = input_list
    length = len(sorted_list)
    bucket = [0] * length
    for d in range(1, MaxBit(sorted_list) + 1):
        count = [0] * 10
        for i in range(0, length):
            count[digit(sorted_list[i], d)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(0, length)[::-1]:
            k = digit(sorted_list[i], d)
            bucket[count[k] - 1] = sorted_list[i]
            count[k] -= 1
        for i in range(0, length):
            sorted_list[i] = bucket[i]
    return sorted_list
