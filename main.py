import numpy as np


def reversed_loop(arr):
    r = []
    last = 0
    a = arr[::-1]
    for x in a:
        r.append(x + last)
        last += x
    return r[::-1]


def sum_first(arr):
    t = sum(arr)
    r = []
    for a in arr:
        r.append(t)
        t -= a
    return r


def generator(arr):
    def gen(a):
        r = 0
        for x in a:
            r += x
            yield r

    return [*gen(arr[::-1])][::-1]


def reverse_sum(arr):
    if not isinstance(arr, list):
        return False
    last = 0
    r = []
    for i in reversed(range(0, len(arr))):
        last = arr[i] + last
        r.append(last)
    return r[::-1]


def josep_joestar(arr):
    if not isinstance(arr, list):
        return False
    for i in range(len(arr) - 2, -1, -1):
        arr[i] += arr[i + 1]
    return arr


def alain_t(arr):
    return np.sum(np.triu(arr), 1)


def user2699(arr):
    return np.add.accumulate(arr[::-1])[::-1]


def stuart(arr):
    return np.flip(np.cumsum(np.flip(arr)))


def stuart_two(arr):
    return np.cumsum(arr[::-1])[::-1]


def student(arr):
    return [sum(arr[i:]) for i in range(len(arr))]


scripts = (
    (reversed_loop, '@sarcoma'),
    (reverse_sum, '@sarcoma'),
    (sum_first, '@sarcoma'),
    (generator, '@sarcoma'),
    (reverse_sum, '@sarcoma'),
    (josep_joestar, '@josep_joestar'),
    # (alain_t, '@alain_t'),
    (user2699, '@user2699'),
    (stuart, '@stuart'),
    (stuart_two, '@stuart_two'),
    # (student, '@student'),
)
