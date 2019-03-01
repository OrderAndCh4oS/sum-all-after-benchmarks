import numpy as np

from timer import timer
from wrap_with import WrapWith


def get_benchmarks(f, wrap_with: WrapWith):
    return (
        (f.__name__, "%.7f" % timer(wrap_with.gen_arr, f),
         'generator, %s' % wrap_with,
         f(range(1, 5))),
        (f.__name__, "%.7f" % timer(wrap_with.gen_arr_to_list, f),
         'generator to List, %s' % wrap_with,
         f(list(range(1, 5)))),
        (f.__name__, "%.7f" % timer(wrap_with.gen_arr_to_np_array, f),
         'generator to np.array, %s' % wrap_with,
         f(np.array(range(1, 5)))),
        (f.__name__, "%.7f" % timer(wrap_with.np_arange, f),
         'np.arange, %s' % wrap_with,
         f(np.arange(1, 5))),
        (f.__name__, "%.7f" % timer(wrap_with.arr_5000, f),
         'list, %s' % wrap_with,
         f([1, 2, 3, 4])),
        (f.__name__, "%.7f" % timer(wrap_with.np_arr_5000, f),
         'np.array, %s' % wrap_with,
         f(np.array([1, 2, 3, 4])))
    )
