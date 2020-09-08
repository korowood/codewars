from itertools import count
from string import ascii_lowercase


def high(x):
    ans = 0
    st = ''
    for let in list(x.split()):
        res = 0
        for word in let:
            res += md[word]
        if res > ans:
            ans = res
            st = let
    return st


md = dict(zip(ascii_lowercase, count(1)))

assert high('man i need a taxi up to ubud') == 'taxi'
assert high('what time are we climbing up the volcano') == 'volcano'
assert high('take me to semynak') == 'semynak'
