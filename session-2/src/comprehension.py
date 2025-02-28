# List comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x * x for x in numbers]
print("Squared:", squared)

# Dictionary comprehension
squared_dict = {x: x * x for x in numbers}
print("Squared Dict:", squared_dict)

# Tuple comprehension (using a generator expression converted to a tuple)
squared_tuple = tuple(x * x for x in numbers)
print("Squared Tuple:", squared_tuple)