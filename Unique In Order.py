def unique_in_order(iterable):
    if len(iterable) >= 1:
        ls = [iterable[0]]
        for i in range(1, len(iterable)):
            if iterable[i] != iterable[i - 1]:
                ls.append(iterable[i])
        return ls
    else:
        return []


assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
