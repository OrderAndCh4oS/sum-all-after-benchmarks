import numpy as np


def sigma_sum_after(n):
    sum_n = n * (n + 1) / 2
    return [int(sum_n - (i * (i + 1) / 2)) for i in range(n)]


def sigma_arange(n):
    return n * (n + 1) / 2 - np.arange(n) * np.arange(1, n + 1) / 2


def sigma_arange_two(n):
    sum_n = n * (n + 1) / 2
    return sum_n - np.arange(n) * np.arange(1, n + 1) / 2


def sigma_arange_three(n):
    sum_n = n * (n + 1) / 2
    return [sum_n - x * (x + 1) / 2 for x in np.arange(n)]


def sigma_range(n):
    sum_n = n * (n + 1) / 2
    return [sum_n - x * (x + 1) / 2 for x in range(n)]


def sigma_recursive(n, i=0, arr=None, sum_n=None):
    if i is n:
        return arr
    if arr is None:
        arr = []
    if sum_n is None:
        sum_n = n * (n + 1) / 2
    arr.append(int(sum_n - (i * (i + 1) / 2)))
    return sigma_recursive(n, i + 1, arr, sum_n)


sigma_scripts = (
    (sigma_sum_after, 'sarcoma'),
    (sigma_arange, 'alain_t'),
    (sigma_arange_two, 'sarcoma'),
    (sigma_arange_three, 'sarcoma'),
    (sigma_range, 'sarcoma'),
    # (sigma_recursive, 'sarcoma'),
)
