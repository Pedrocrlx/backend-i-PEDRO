def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def factorial(x: int) -> int:
    if x < 0:
        raise AssertionError("vai joreg mete num")
    result = 1
    for i in range(2, x + 1):
        result *= i
    # return print(f"factorial number of {x} are -> {result}")
    return result

factorial(6)
