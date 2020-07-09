small_letters = list(map(chr, range(ord('a'), ord('z') + 1)))

mydict = {}
for i in range(len(small_letters)):
    mydict[small_letters[i]] = i + 1


def alphabet_position(text):
    text = text.lower()
    text = filter(lambda char: char not in " ?.!/;:'", text)
    # ml = []
    st = ''
    for word in text:
        # ml.append(mydict[word])
        st += str(mydict[word]) + ' '
    return st[:-1]


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position(""))
