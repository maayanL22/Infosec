def quine():
    pass
    s = 's = %r\nprint(s %% s)'
    print(s % s)
    return s
