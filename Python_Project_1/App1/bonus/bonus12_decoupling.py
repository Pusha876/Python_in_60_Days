feet_inches = input("Enter feet and inches: ")


def convert(feet_inches_input):
    parts = feet_inches_input.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    return f"{feet} feet and {inches} inches is equal to {meters} meters."


result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
