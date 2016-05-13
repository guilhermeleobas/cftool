

def format_time(val):
    ms = 1
    s = 1000 * ms
    m = 60 * s
    h = 60 * m

    if (val >= h):
        return str(int(round(val / h))) + 'h'
    elif (val >= m):
        return str(int(round(val / m))) + 'm'
    elif (val >= s):
        return str(int(round(val / s))) + 's'
    else:
        return str(int(round(val))) + 'ms'
