def outer_funct():
    x = 10

    def inner_funct():
        nonlocal x
        # x += 5
        x = x + 5
        y = 10
        print("inner function: x = ", x, ",y =", y)

    inner_funct()
    print("outer function: =", x)


outer_funct()
