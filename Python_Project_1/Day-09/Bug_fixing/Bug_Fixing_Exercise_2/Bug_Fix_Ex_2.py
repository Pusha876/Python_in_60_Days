# The print function should be unindented because we don't want the for-loop
# to call the function multiple times.
# We want to print the value of x after the for-loop
# has finished its iterations.

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for identifier in ids:
    if '_' in identifier:
        x = x + 1
print(x)
