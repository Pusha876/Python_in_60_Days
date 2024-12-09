file = open("essay.txt", "r", encoding="utf-8")
content = file.read()
file.close()

num_words = len(content)
print(num_words)
