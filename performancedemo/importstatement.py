import cProfile
import string


def doit1():
    import string
    string.lower('PYTHON')


def slow():
    for i in xrange(100000):
        doit1()


def doit2():
    string.lower('PYTHON')


def fast():
    for i in xrange(100000):
        doit2()


print('repetitive imports')
print('############')
cProfile.run('slow()')


print('single import')
print('############')
cProfile.run('fast()')
