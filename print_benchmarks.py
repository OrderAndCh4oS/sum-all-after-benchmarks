import numpy as np

from get_benchmarks import get_benchmarks
from main import scripts
from timer import timer
from wrap_with import WrapWith


def print_benchmarks(wrap_with):
    for script in scripts:
        print(script[0].__name__)
        for benchmark in get_benchmarks(script[0], wrap_with):
            if benchmark[3] is not False:
                print("%s <- %s = %s" % (benchmark[1], benchmark[2], benchmark[3]))


make_range = timer(range, 5000)
make_list = timer(list, range(5000))
make_np_range = timer(np.arange, 5000)
make_np_array = timer(np.array, range(5000))

print('Array Creation Overhead\n-----------------------\n')

print('Make range: %.6f' % make_range)
print('Make np.arange: %.6f\n' % make_np_range)

print('Make list: %.6f' % make_list)
print('Make np_array: %.6f\n\n' % make_np_array)

print('Benchmark\n---------\n')

print_benchmarks(WrapWith(4))

# print('sigma_sum_after:\n')
# print("%.6f - With n\n" % timer(sigma_sum_after, 5000))
#
# print('sigma_arange:\n')
# print("%.6f - With n\n" % timer(sigma_arange, 5000))
#
# print('sigma_arange_two:\n')
# print("%.6f - With n\n" % timer(sigma_arange_two, 5000))
#
# print('sigma_arange_three:\n')
# print("%.6f - With n\n" % timer(sigma_arange_three, 5000))
#
# print('sigma_range:\n')
# print("%.6f - With n\n" % timer(sigma_range, 5000))
#
# print('reversed:', print_benchmark(reversed_loop))
# # print('reverse_sum:', print_benchmark(reverse_sum))
# print('sum_first:', print_benchmark(sum_first))
# print('generator:', print_benchmark(generator))
# print('user2699:', print_benchmark(user2699))
# print('stuart:', print_benchmark(stuart))
# print('stuart_two:', print_benchmark(stuart_two))
# # print('josep_joestar', print_benchmark(josep_joestar))
# # print('alain_t: Too slow to test')
# # print('student: Too slow to test')
#
# print('Proofs\n------\n')
#
# short_arr = list(range(1, 5))
#
# print('sigma_sum_after', sigma_sum_after(4))
# print('sigma_arange', sigma_arange(4))
# print('sigma_arange_two', sigma_arange_two(4))
# print('sigma_arange_three', sigma_arange_three(4))
# print('sigma_range', sigma_range(4))
# print('sigma_recursive', sigma_recursive(4))
# print('reversed', reversed_loop(short_arr))
# # print('reverse_sum', reverse_sum(short_arr))
# print('sum_first', sum_first(short_arr))
# print('generator', generator(short_arr))
# print('user2699', user2699(short_arr))
# print('stuart', stuart(short_arr))
# print('stuart_two', stuart_two(short_arr))
# # print('josep_joestar', josep_joestar(short_arr))
