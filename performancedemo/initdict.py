import cProfile
import uuid


words = [str(uuid.uuid4()) for i in xrange(100000)]*100


def slow():
    wdict = {}
    for word in words:
        if word not in wdict:
            wdict[word] = 0
        wdict[word] += 1


def fast():
    wdict = {}
    for word in words:
        try:
            wdict[word] += 1
        except KeyError:
            wdict[word] = 1


print('Using if')
print('############')
cProfile.run('slow()')


print('Using try')
print('############')
cProfile.run('fast()')
