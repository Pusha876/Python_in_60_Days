file = open("essay.txt", "r", encoding="utf-8")
content = file.read()
file.close()

print(content.title())
