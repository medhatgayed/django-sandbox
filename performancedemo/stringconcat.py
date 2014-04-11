import cProfile


a = ['x' for i in range(10000000)]


def slow():
    r = ''
    for x in a:
        r += x


def fast():
    r = ''.join(a)


print('Using +')
print('############')
cProfile.run('slow()')


print('Using .join()')
print('############')
cProfile.run('fast()')
