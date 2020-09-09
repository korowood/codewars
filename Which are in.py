def in_array(array1, array2):
    """
    Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of
    the strings of a1 which are substrings of strings of a2.
    """
    ms = set()
    for word1 in array1:
        for word2 in array2:
            if word1 in word2:
                ms.add(word1)
    return sorted(list(ms))


a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']

assert in_array(a1, a2) == r
