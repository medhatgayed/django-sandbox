import cProfile


def slow(a):
    sorted(a)


def fast(a):
    a.sort()


print('Using sorted(list)')
print('############')
a = [i for i in range(10000000)]
cProfile.run('slow(a)')


print('Using list.sort()')
print('############')
a = [i for i in range(10000000)]
cProfile.run('fast(a)')
