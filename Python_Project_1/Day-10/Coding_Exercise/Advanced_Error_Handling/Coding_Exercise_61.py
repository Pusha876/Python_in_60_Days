# This program has two exceptions. The first exception is a ValueError
# exception, which is raised when the user enters a string instead of a number.
# The second
# exception is a ZeroDivisionError exception, which is raised when the user
# enters a zero as the total value. Add a try-except block to handle the
# ZeroDivisionError exception. If the user enters a zero as the total value,
# the program should print "Your total value cannot be a zero."

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total_value * 100

    print(f"That is {percentage}%")

except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be a zero.")
