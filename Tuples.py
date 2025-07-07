
# Creating a tuple with multiple elements
person = ("Alice", 30, "Engineer")

# Accessing elements in a tuple
name = person[0]  # "Alice"
age = person[1]   # 30

# Tuples are immutable, so you cannot change their elements
# person[1] = 31  # This would raise a TypeError

# Tuples can be used to return multiple values from a function
def get_min_max(numbers):
    return (min(numbers), max(numbers))

result = get_min_max([3, 1, 4, 2])
# result is (1, 4)

# Tuple unpacking
min_val, max_val = result  # min_val = 1, max_val = 4

# Tuples can be nested
nested = (1, (2, 3), 4)

print("Name:", name)
print("Age:", age)
print("Min value:", min_val)
print("Max value:", max_val)
print("Nested tuple:", nested)
# Output:
# Name: Alice
# Age: 30
# Min value: 1
# Max value: 4

