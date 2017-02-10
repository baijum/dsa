def decimal_to_binary(val):
    if val == 0:
        return "0"
    out = []
    while val >= 1:
        rem = val % 2 
        val = val / 2
        out.append(str(rem))

    out.reverse()
    return "".join(out)
