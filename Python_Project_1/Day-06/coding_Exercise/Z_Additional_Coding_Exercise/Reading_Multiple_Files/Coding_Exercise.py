filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"C:/Users/Jamie/Downloads/{filename}", "r", encoding="utf-8")
    content = file.read()
    print(content)
