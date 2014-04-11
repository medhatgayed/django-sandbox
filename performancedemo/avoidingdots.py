import cProfile


oldlist = ['abcdefghijklmnopqrstuvwxyz' for i in xrange(1000000)]


def slow():
    newlist = []
    for word in oldlist:
        newlist.append(word.upper())


def fast():
    newlist = []
    append = newlist.append
    upper = str.upper
    for word in oldlist:
        append(upper(word))


print('Using dots in loop')
print('############')
cProfile.run('slow()')


print('Using no dots in loop')
print('############')
cProfile.run('fast()')
