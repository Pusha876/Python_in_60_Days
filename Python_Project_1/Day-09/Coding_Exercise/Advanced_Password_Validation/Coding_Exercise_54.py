# This program is a simple password validation program.
# It checks if the password is equal to or at least 8 characters long.
# If it is greater than 7 characters, it prints "Great password there!".
# If it is equal to 7 characters, it prints "Password is OK, but not too
# strong".
# If it is not, it prints "Your password is weak.".

password = input("Enter new password: ")

if len(password) > 7:
    print("Great password there")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak")
