# You are printing out the password with less than 8 characters.

passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]

for i in passwords:
    if len(i) < 8:
        print(i)
