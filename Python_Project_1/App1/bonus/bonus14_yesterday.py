from Python_Project_1.App1.bonus.bonus14_parsers import parse
from Python_Project_1.App1.bonus.bonus14_convert import convert

feet_inches = input("Enter feet and inches: ")


parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
