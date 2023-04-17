from itertools import product


def solution(word):
    li = []
    for i in range(5):
        for c in product('AEIOU', repeat=i + 1):
            li.append(''.join(c))

    return sorted(li).index(word) + 1