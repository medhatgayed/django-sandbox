import cProfile


oldlist = ['abcdefghijklmnopqrstuvwxyz' for i in xrange(1000000)]


def slow():
    newlist = []
    for word in oldlist:
        newlist.append(word.upper())


def fast():
    newlist = map(str.upper, oldlist)


def fast2():
    newlist = [s.upper() for s in oldlist]


print('Using for loop')
print('############')
cProfile.run('slow()')


print('Using map()')
print('############')
cProfile.run('fast()')


print('Using list comprehension')
print('############')
cProfile.run('fast2()')
