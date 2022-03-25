def calc(a, b):
    print(a, "--", b)
    cf = b - a
    a = 100 / (a + b) * a
    b = 100 - a
    c = (b - a) / cf
    # print(int(c))
    a = (b - c) / 2
    b = 100 - a
    return print(int(a), "-", int(b))


calc(1, 2)
calc(2, 4)
calc(5, 10)
calc(10, 20)
calc(2, 3)
calc(6, 9)
calc(2, 7)
calc(7, 9)
