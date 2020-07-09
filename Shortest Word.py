def find_short(s):
    s = list(s.split())
    s.sort(key=lambda x: len(x))
    return len(s[0])


a = find_short("bitcoin take over the world maybe who knows perhaps")
st = "bitcoin take over the world maybe who knows perhaps"
print(a)
