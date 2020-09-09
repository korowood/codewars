def solution(s):
    if len(s) == 0:
        return []
    else:
        ls = []
        while len(s) >= 2:
            ls.append(s[:2])
            s = s[2:]
        if len(s) == 1:
            ls.append(s + '_')
        return ls




tests = (
    (1, "asdfadsf", ['as', 'df', 'ad', 'sf']),
    (2, "asdfads", ['as', 'df', 'ad', 's_']),
    (3, "", []),
    (4, "x", ["x_"]),
)

for i, inp, exp in tests:
    assert solution(inp) == exp
    print("TEST {} is OK".format(i))
