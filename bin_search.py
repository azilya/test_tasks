
def binary_search(arr, n):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if n > arr[mid]:
            left = mid + 1
        elif n < arr[mid]:
            right = mid - 1
        else:
            return mid
    return -1


def binary_search_recursive_leftmost(arr, n, left, right):
    if left < right:
        mid = (left + right) // 2
        if n > arr[mid]:
            return binary_search_recursive_leftmost(arr, n, mid + 1, right)
        else:
            return binary_search_recursive_leftmost(arr, n, left, mid)
    if arr[left] == n:
        return left
    return -1


arr = [1, 10, 23]
n = 15
print(binary_search(arr, n))
print(binary_search_recursive_leftmost(arr, n, 0, len(arr)))
