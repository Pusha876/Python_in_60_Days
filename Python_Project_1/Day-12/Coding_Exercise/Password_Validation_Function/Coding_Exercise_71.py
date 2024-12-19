# The function should return a string that describes the password strength.
# We're using a simple rule to determine the strength of the password.
# A password is strong if it meets all of the following conditions:

def strength(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False
    digit = False
    uppercase = False
    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"
