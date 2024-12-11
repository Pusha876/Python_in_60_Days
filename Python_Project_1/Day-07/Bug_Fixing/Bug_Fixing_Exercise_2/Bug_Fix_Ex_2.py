# This program had the integer referencing the variable and not the items
# in the list.

numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)
