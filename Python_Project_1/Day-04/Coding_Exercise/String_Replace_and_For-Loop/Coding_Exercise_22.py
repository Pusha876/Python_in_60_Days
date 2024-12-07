# This code snippet replaces the white space of each string with an underscore.

usernames = ['the blueman', 'sorted hedgehog', 'infinite lagoon']

for username in usernames:
    username = username.replace(' ', "_")
    print(username)
