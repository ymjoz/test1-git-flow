import inspect


def g(data):
    return data * data


def f(x):
    breakpoint()
    lst = []
    for i in range(x):
        # frame = inspect.currentframe()
        val = g(i)
        lst.append(val)
    return lst


print(f(3))
