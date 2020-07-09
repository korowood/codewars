def find_outlier(integers):
    integers.sort(key=lambda x: x % 2)
    return integers[-1] if not integers[-2] % 2 else integers[0]


a = find_outlier([2, 4, 6, 3, 10, 8])
b = find_outlier([160, 3, 1719, 19, 11, 13, -21])
print(b)