# This code was trying to read a file that did not exist.
# file needed to be created first before reading it.

file = open("data.txt", "w", encoding='utf-8')
file.write("100.12")
file.close()
