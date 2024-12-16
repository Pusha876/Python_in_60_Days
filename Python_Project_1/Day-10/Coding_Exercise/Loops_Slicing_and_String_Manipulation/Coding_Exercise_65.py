# This program will print the filenames capitalized without the extension.

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for i in filenames:
    print(i[:-4].capitalize())
