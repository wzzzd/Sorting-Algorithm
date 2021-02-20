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


# 快速排序
def quickSort(nums): 
    """
    思路：
        基准：从数列中挑出一个元素，称为 “基准”（pivot）;
        分区：
            重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）；
            在这个分区退出之后，该基准就处于数列的中间位置；
        递归：递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列，按照上述步骤排序；
    备注：这种写法的平均空间复杂度为 O(nlogn)
    @param nums: 待排序数组
    @param left: 数组上界
    @param right: 数组下界
    """
    if len(nums) <= 1:
        return nums
    pivot = nums[0]                                         # 基准值
    left = [nums[i] for i in range(1, len(nums)) if nums[i] < pivot] 
    right = [nums[i] for i in range(1, len(nums)) if nums[i] >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)

def quickSort2(nums, left, right):  
    """
    这种写法的平均空间复杂度为 O(logn) 
    @param nums: 待排序数组
    @param left: 数组上界
    @param right: 数组下界
    """
    # 分区操作
    def partition(nums, left, right):
        pivot = nums[left]                                  # 基准值
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]                        # 比基准小的交换到前面
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]                        # 比基准大交换到后面
        nums[left] = pivot                                  # 基准值的正确位置，也可以为 nums[right] = pivot
        return left                                         # 返回基准值的索引，也可以为 return right
    # 递归操作
    if left < right:
        pivotIndex = partition(nums, left, right)
        quickSort2(nums, left, pivotIndex - 1)              # 左序列
        quickSort2(nums, pivotIndex + 1, right)             # 右序列
    return nums


# 堆排序
# 大根堆（从小打大排列）
def heapSort(nums):
    """
    堆排序：
        大根堆：每个节点的值都大于或等于其子节点的值，用于升序排列；
        小根堆：每个节点的值都小于或等于其子节点的值，用于降序排列。
    思路：
        此代码采用大根堆的思想
        1.创建一个堆 H[0……n-1]；
        2.把堆首（最大值）和堆尾互换；
        3.把堆的尺寸缩小 1，并把新的数组顶端元素 调整到相应位置；
        4.重复步骤2，直到堆的尺寸为1。
    备注：python中，基本数据类型，不能在内部函数中赋值，而非基本类型，如list、dict等，可以在内部函数中，修改某个索引值
    """
    # 调整堆
    def adjustHeap(nums, i, size):
        # 非叶子结点的左右两个孩子
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        # 在当前结点、左孩子、右孩子中找到最大元素的索引
        largest = i 
        if lchild < size and nums[lchild] > nums[largest]:  # 左子节点 > 父节点
            largest = lchild 
        if rchild < size and nums[rchild] > nums[largest]:  # 右子节点 > 父节点
            largest = rchild 
        # 如果最大元素的索引不是当前结点，把大的结点交换到上面，继续调整堆
        if largest != i: 
            nums[largest], nums[i] = nums[i], nums[largest]
            # 第 2 个参数传入 largest 的索引是交换前大数字对应的索引
            # 交换后该索引对应的是小数字，应该把该小数字向下调整
            adjustHeap(nums, largest, size)
    # 建立堆
    def builtHeap(nums, size):
        for i in range(len(nums)//2)[::-1]:                 # 从倒数第一个非叶子结点开始建立大根堆
            adjustHeap(nums, i, size)                       # 对所有非叶子结点进行堆的调整
        # print(nums)                                       # 第一次建立好的大根堆
    # 堆排序 
    size = len(nums)
    builtHeap(nums, size) 
    for i in range(len(nums))[::-1]:                        # [::-1]将数组倒序
        # 每次根结点都是最大的数，最大数放到后面
        nums[0], nums[i] = nums[i], nums[0] 
        # 交换完后还需要继续调整堆，只需调整根节点，此时数组的 size 不包括已经排序好的数
        adjustHeap(nums, 0, i) 
    return nums                                             # 由于每次大的都会放到后面，因此最后的 nums 是从小到大排列


# 计数排序
def countingSort(nums):
    """
    计数排序：计数排序要求输入数据的范围在 [0,N-1] 之间，则可以开辟一个大小为 N 的数组空间，将输入的数据值转化为键存储在该数组空间中，数组中的元素为该元素出现的个数。
    思路：
        1. 花O(n)的时间扫描一下整个序列 A，获取最小值 min 和最大值 max
        2. 开辟一块新的空间创建新的数组 B，长度为 ( max - min + 1)
        3. 数组 B 中 index 的元素记录的值是 A 中某元素出现的次数
        4. 最后输出目标整数序列，具体的逻辑是遍历数组 B，输出相应元素以及对应的个数
    """
    bucket = [0] * (max(nums) + 1)                          # 桶的个数
    for num in nums:                                        # 将元素值作为键值存储在桶中，记录其出现的次数
        bucket[num] += 1
    i = 0                                                   # nums 的索引
    for j in range(len(bucket)):
        while bucket[j] > 0:                                # 当bucket的元素值，大于0，那么继续从里面取数
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums


# 桶排序
def bucketSort(nums, defaultBucketSize = 5):
    """
    桶排序：计数排序的升级版，利用函数的映射关系，将数组中的元素映射到对应的桶中，再使用排序算法对每个桶进行排序。
    思路：
        1. 设置固定数量的空桶。
        2. 把数据放到对应的桶中。
        3. 对每个不为空的桶中数据进行排序。
        4. 拼接不为空的桶中数据，得到结果
    """
    maxVal, minVal = max(nums), min(nums)
    bucketSize = defaultBucketSize                          # 如果没有指定桶的大小，则默认为5
    bucketCount = (maxVal - minVal) // bucketSize + 1       # 数据分为 bucketCount 组
    buckets = []                                            # 创建空的二维桶
    for i in range(bucketCount):
        buckets.append([])
    # 利用函数映射将各个数据放入对应的桶中
    for num in nums:
        buckets[(num - minVal) // bucketSize].append(num)   # 放进对应的桶里
    nums.clear()                                            # 清空 nums
    # 对每一个二维桶中的元素进行排序
    for bucket in buckets:
        insertionSort(bucket)                               # 假设使用插入排序
        nums.extend(bucket)                                 # 将排序好的桶依次放入到 nums 中
    return nums


# 基数排序
def radixSort(nums):
    """
    基数排序：桶排序的一种推广，考虑待排序记录的多个关键维度。
        1. MSD（主位优先法）：从高位开始进行排序
        2. LSD（次位优先法）：从低位开始进行排序
    思路：
        (LSD法)
        1. 将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零
        2. 从最低位开始，依次进行一次排序
        3. 从最低位排序一直到最高位排序完成以后, 数列就变成一个有序序列
    """
    mod = 10
    div = 1
    mostBit = len(str(max(nums)))                           # 最大数的位数决定了外循环多少次
    buckets = [[] for row in range(mod)]                    # 构造 mod 个空桶
    while mostBit:
        for num in nums:                                    # 将数据放入对应的桶中
            buckets[num // div % mod].append(num)
        i = 0                                               # nums 的索引
        for bucket in buckets:                              # 将数据收集起来
            while bucket:
                nums[i] = bucket.pop(0)                     # 依次取出
                i += 1
        div *= 10
        mostBit -= 1
    return nums


a = [2,4,6,1,3,9,10,33,2,60,8,20]
result = radixSort(a)
print(result)

