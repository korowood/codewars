def move_zeros(array):
    array.sort(key=lambda x: x == 0 and num(x), reverse=False)
    return array


def num(x):
    if type(x) == float:
        new_x = str(int(x))
    else:
        new_x = str(x)
    return True if new_x.isdigit() else False


def assert_equals(arr1, arr2):
    if arr1 == arr2:
        return True
    else:
        return False


print(assert_equals(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]))
print(assert_equals(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                    [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(assert_equals(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                    ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(
    assert_equals(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]),
                  ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(assert_equals(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0]))
print(assert_equals(move_zeros(["a", "b"]), ["a", "b"]))
print(assert_equals(move_zeros(["a"]), ["a"]))
print(assert_equals(move_zeros([0, 0]), [0, 0]))
print(assert_equals(move_zeros([0]), [0]))
print(assert_equals(move_zeros([False]), [False]))
print(assert_equals(move_zeros([]), []))
