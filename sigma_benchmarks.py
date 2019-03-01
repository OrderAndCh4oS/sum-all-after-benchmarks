from sigma import sigma_scripts
from timer import timer


def get_benchmarks(f, n):
    return f.__name__, "%.7f" % timer(f, n), 'sigma, N = %d' % n, f(4)


benchmarks = []

for script in sigma_scripts:
    benchmarks.append((get_benchmarks(script[0], 10000), script[1]))

benchmarks.sort(key=lambda val: val[0][1])
print('N = 10000')
for benchmark in benchmarks:
    print("%s | %s" % (benchmark[0][1], benchmark[0][0]))
