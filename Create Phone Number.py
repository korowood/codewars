def create_phone_number(n):
    str_n = ''.join(map(str, n))
    ans = "(" + str_n[:3] + ") " + str_n[3:6] + "-" + str_n[6:]
    return ans


a = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(a)

# (123) 456-7890
