a = [0, 0, 5, 5, 0, 0]
a1 = [0, -1, -1, 5, -5, 1, 2]
a2 = [1, 2, -5, 1, 2, -1]

# [0, 0, 0, 0, 5, 5]

def three_point(arr):
    count = 0
    arr = sorted(arr)
    print(arr)
    for i in range(len(arr) - 1):
        """
        for j in range(i + 1, len(arr)):
            k = len(arr) - 1
            while j < k:
                sum = arr[i] + arr[j] + arr[k]
                if sum == 0:
                    print(i, j, k)
                    count += 1
                if sum >= 0:
                    k -= 1
                elif sum < 0:
                    j += 1
        """
        j = i + 1
        k = len(arr) - 1
        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum == 0:
                print(i, j, k)
                count += 1
            if sum >= 0:
                k -= 1
            elif sum < 0:
                j += 1
    print(count)


three_point(a1)


def zero_sum(arr):
    map = {}
    sum = 0
    ans = []
    for i in range(len(arr) + 1):
        if sum not in map:
            map[sum] = [i]
        else:
            for j in map[sum]:
                ans.append((j, i-1))
            map[sum].append(i)
        if i < len(arr): sum += arr[i]
    print(ans)


zero_sum(a2)