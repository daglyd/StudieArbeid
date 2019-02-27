from random import randint


def exact_frequencies():
    frequencies = {}
    for s in range(2, 13):
        frequency = 0
        for d1 in range(1, 7):
            for d2 in range(1, 7):
                if d1 + d2 == s:
                    frequency += 1
        frequencies[s] = frequency
    return frequencies


def calc_frequencies(N):
    frequencies = {i: 0 for i in range(2, 13)}
    for exp in range(N):
        d1, d2 = randint(1, 6), randint(1, 6)
        frequencies[d1 + d2] += 1
    frequencies = {i: j * 36 / float(N) for (i, j) in frequencies.iteritems()}
    return frequencies

exact_frequencies = exact_frequencies()
approx_frequencies = calc_frequencies(1000000)
print exact_frequencies
