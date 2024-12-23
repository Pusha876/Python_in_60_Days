# This glob module is used to retrieve files/pathname
# matching a specified pattern.

import glob

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r', encoding='utf-8') as file:
        print(file.read().upper())
