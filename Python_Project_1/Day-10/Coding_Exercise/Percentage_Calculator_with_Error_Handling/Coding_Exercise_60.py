# This program calculates the percentage of a value in relation to a total
# value.
# It also handles errors if the user enters a string instead of a number.

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total_value * 100

    print(f"That is {percentage}%")

except ValueError:
    print("You need to enter a number. Run the program again.")
