# The conditional block should be indented properly.
# The code should be like this:

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for identifier in ids:
    if '_' in identifier:
        x = x + 1
print(x)
