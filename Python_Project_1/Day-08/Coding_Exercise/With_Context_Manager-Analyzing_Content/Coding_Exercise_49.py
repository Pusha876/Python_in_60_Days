with open("essay.txt", 'r', encoding='utf-8') as file:
    content = file.read()

nr_chars = len(content)
print(nr_chars)
