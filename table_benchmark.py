from get_benchmarks import get_benchmarks
from main import scripts
from wrap_with import WrapWith


def table_benchmark(wrap_with):
    benchmarks = []
    for script in scripts:
        benchmarks.append(get_benchmarks(script[0], wrap_with))

    for i in range(6):
        results = [benchmark[i] for benchmark in benchmarks]
        results.sort(key=lambda val: val[1])
        print('\n')
        print(results[0][2])
        print('-------------------------')
        for result in results:
            if result[3] is not False:
                print("%s | %s" % (result[1], result[0]))


table_benchmark(WrapWith(4))
table_benchmark(WrapWith(500))
table_benchmark(WrapWith(2500))
