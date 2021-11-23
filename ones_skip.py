arrays = [
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 1],
    [0, 0],
]


def longest_seq(array):
    ind = ind_tmp = ind_max = 0
    for item in array:
        if item == 1:
            ind += 1
        else:
            total = ind_tmp + ind
            ind_max = max(ind_max, total)
            ind_tmp = ind
            ind = 0
    total = ind_tmp + ind
    ind_max = max(ind_max, total)
    return ind_max


for array in arrays:
    print(longest_seq(array))
