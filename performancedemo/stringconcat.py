import cProfile
import timeit


a = ['x' for i in range(10000000)]


def fast_concat():
    r = ''.join(a)


def slow_concat():
    r = ''
    for x in a:
        r += x


print('Fast Concat:')
print('############')
timeit.timeit(setup='from __main__ import fast_concat', stmt='fast_concat()')
cProfile.run('fast_concat()')

print('Slow Concat:')
print('############')
timeit.timeit(setup='from __main__ import slow_concat', stmt='slow_concat()')
cProfile.run('slow_concat()')