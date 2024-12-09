file = open("essay.txt", "r", encoding="utf-8")
content = file.read()
file.close()

num_words = len(content)
message = f"The file contains {num_words} characters."

print(message)
