# This code needed to end the line with '\n' to write the data in a new line.

file = open("data.txt", 'w', encoding='utf-8')

file.write("100.12\n")
file.write("111.23\n")

file.close()
