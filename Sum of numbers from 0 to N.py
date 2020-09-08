def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return str(n) + "<0"
    else:
        counter = sum(range(n + 1))
        return '+'.join(map(str, range(n + 1))) + " = " + str(counter)


tests = (
    (6, "0+1+2+3+4+5+6 = 21"),
    (7, "0+1+2+3+4+5+6+7 = 28"),
    (0, "0=0"),
    (-1, "-1<0"),
    (-10, "-10<0"),
)

for inp, exp in tests:
    assert (show_sequence(inp) == exp)
