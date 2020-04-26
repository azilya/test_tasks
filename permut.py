# -*- coding = utf8 -*-
from collections import OrderedDict


def permute(nums):
    permutations = OrderedDict()

    def work(head, tail):
        if not tail and tuple(head) not in permutations:
            permutations[tuple(head)] = 0
        else:
            for i in range(len(tail)):
                work(head + [tail[i]], tail[:i]+tail[i+1:])
    work([], nums)
    return permutations.keys()


def powerset(nums):
    powerset = OrderedDict()

    def work(head, tail, size):
        if len(head) == size:
            if tuple(head) not in powerset:
                powerset[tuple(head)] = 0
        else:
            for i in range(len(tail)):
                work(head + [tail[i]], tail[i+1:], size)
    for i in range(len(nums)+1):
        work([], nums, i)
    return powerset.keys()


print(permute([1, 2, 2, 3]))
print(powerset([1, 2, 2]))
