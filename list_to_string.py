def l2s(lst: list) -> str:
    s = '['
    l = len(lst)
    for e in lst:
        s = s + str(e)
        l = l - 1
        if l > 0:
            s = s + ', '
    s = s + ']'
    return s
