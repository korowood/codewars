def make_readable(seconds):
    """
    Write a function, which takes a non-negative integer (seconds) as input and returns the time in a
    human-readable format (HH:MM:SS)
    """
    h = seconds / 60 ** 2
    m = (seconds % 60 ** 2) / 60
    s = (seconds % 60 ** 2 % 60)
    return "%02d:%02d:%02d" % (h, m, s)


assert make_readable(0) == "00:00:00"
assert make_readable(5) == "00:00:05"
assert make_readable(60) == "00:01:00"
assert make_readable(86399) == "23:59:59"
assert make_readable(359999) == "99:59:59"
