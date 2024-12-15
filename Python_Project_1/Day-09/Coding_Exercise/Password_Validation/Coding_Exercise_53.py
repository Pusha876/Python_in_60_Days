# This is a password validation program.
# It checks if the password is at least 8 characters long.

password = input("Enter new password: ")

if len(password) >= 8:
    print("Great password there!")
else:
    print("Your password is weak.")
