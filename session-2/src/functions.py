def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print("function that accepts any number of numeric arguments (using *args)", sum(1, 2, 3))


def filterValues(**kwargs):
    return kwargs.values()


print(filterValues(a="apple", b="banana"))
