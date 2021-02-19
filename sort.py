# -*- encoding: UTF-8 -*-





# 冒泡排序
def bubbleSort(nums):
    """
    冒泡排序：每次与相邻的元素组成二元组进行大小对比，将较大的元素排到右边，小的元素排到左边，直至迭代完数组。
    备注：将排好序的元素，放到最后面
    """
    for i in range(len(nums) - 1):                          # 遍历 len(nums)-1 次
        for j in range(len(nums) - i - 1):                  # 已排好序的部分不用再次遍历
            if nums[j] > nums[j+1]:     
                nums[j], nums[j+1] = nums[j+1], nums[j]     # Python 交换两个数不用中间变量，将大的数排到后面
    return nums


# 选择排序
def selectionSort(nums):
    """
    选择排序：每次在后面的元素中，选取最小的元素，并插入到前面已经排好序的列表最右方。
    备注：将排好序的元素，放到最前面
    """
    for i in range(len(nums) - 1):                          # 遍历 len(nums)-1 次
        minIndex = i                                        # 记录最小的元素index
        for j in range(i + 1, len(nums)):                   # 排好序的元素，放到最前面
            if nums[j] < nums[minIndex]:                    # 更新最小值索引
                minIndex = j                                # 修改最小值元素的index
        nums[i], nums[minIndex] = nums[minIndex], nums[i]   # 把最小数交换到前面
    return nums


# 插入排序
def insertionSort(nums):
    """
    插入排序：每次将后面的元素，插到前面已经排好序的元素中；
    备注：将排好序的元素，放到最前面
    优化：后面的插入算法，可以使用二分查找法进行计算次数的优化。
    """
    for i in range(len(nums) - 1):                          # 遍历 len(nums)-1 次
        curNum, preIndex = nums[i+1], i                     # curNum 保存当前待插入的数，i为当前元素的index
        while preIndex >= 0 and curNum < nums[preIndex]:    # 将比 curNum 大的元素向后移动
            nums[preIndex + 1] = nums[preIndex]             # 将当前位置的值，赋值给下一个位置
            preIndex -= 1                                   # 索引往左退一位
        nums[preIndex + 1] = curNum                         # 待插入的数的正确位置   
    return nums


# 希尔排序
def shellSort(nums):
    """
    希尔排序：是插入排序的一种更高效率的实现。不同之处，在于它优先比较距离较远的元素
    备注：核心在于间隔序列的设定，可提前设定，也可动态设定
    """
    lens = len(nums)
    gap = 1  
    while gap < lens // 3:
        gap = gap * 3 + 1                                   # 动态定义间隔序列
    while gap > 0:
        for i in range(gap, lens):
            curNum, preIndex = nums[i], i - gap             # curNum 保存当前待插入的数
            while preIndex >= 0 and curNum < nums[preIndex]:
                nums[preIndex + gap] = nums[preIndex]       # 将比 curNum 大的元素向后移动
                preIndex -= gap
            nums[preIndex + gap] = curNum                   # 待插入的数的正确位置
        gap //= 3                                           # 下一个动态间隔
    return nums


# 归并排序
def mergeSort(nums):
    """
    归并排序：一种分而治之的思想应用，有两种实现方法：自上而下的递归、自下而上的迭代
    """
    # 归并过程
    def merge(left, right):
        result = []                                         # 保存归并后的结果
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:                         # 比较左右元素的大小
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:]              # 剩余的元素直接添加到末尾
        return result
    # 递归过程
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2                                    # 取中位数
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)










a = [2,4,6,1,3,9,10,33,2,60,8,20]
# result = bubbleSort(a)
result = mergeSort(a)

print(result)

