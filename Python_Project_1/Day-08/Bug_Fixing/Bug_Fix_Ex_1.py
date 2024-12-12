# If the read() method is called two times, it returns an empty string the
# second time.
# To avoid that, we call the read() method once and store its output
# in a variable:

with open("file.txt", 'r', encoding='utf-8') as file:
    content = file.read()

print(content)
print(len(content))
