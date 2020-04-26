############
# Heap sort
############


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]

        # heapify root element
        heapify(arr, i, 0)


#############
# Merge Sort
#############
def merge(l1, l2):
    res = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))
    return res + l1 + l2


def mergeSort(nums):
    if len(nums) == 1:
        return nums
    left = nums[:len(nums)//2]
    right = nums[len(nums)//2:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)


#############
# Quick sort
#############
def get_partition(nums, start, end) -> int:
    left = start
    pivot = nums[end]
    for right in range(start, end):
        if nums[right] < pivot:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    nums[left], nums[end] = nums[end], nums[left]
    return left


def _quick_sort(nums, start, end):
    if start < end:
        partition = get_partition(nums, start, end)
        _quick_sort(nums, start, partition-1)
        _quick_sort(nums, partition+1, end)


def quick_sort(nums):
    _quick_sort(nums, 0, len(nums)-1)


##############
# N^2 sorting
##############
def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]


def selectionSort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[min], nums[i] = nums[i], nums[min]


def insertionSort(nums):
    for index in range(1, len(nums)):
        position = index
        currentvalue = nums[index]

        while position > 0 and nums[position-1] > currentvalue:
            nums[position] = nums[position-1]
            position -= 1

        nums[position] = currentvalue
