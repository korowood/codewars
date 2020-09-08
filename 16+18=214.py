def add(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 + num2
    else:
        st = ''
        while num1 >= 10 or num2 >= 10:
            a1, a2 = num1 % 10, num2 % 10
            st = str(a1 + a2) + st
            num1 //= 10
            num2 //= 10
        st = str(num1 + num2) + st
        return st


# print(add(122, 81))
# print(add(26, 39))
# print(add(16, 18))

def real_addition_test():
    assert add(2, 11) == 13
    assert add(0, 1) == 1
    assert add(0, 0) == 0


# real_addition_test()


def silly_addition_test():
    assert add(16, 18), 214
    assert add(26, 39), 515
    assert add(122, 81), 1103


silly_addition_test()
