with open("story.txt", "r", encoding="utf-8") as file:
    content = file.read()

with open("story_copy.txt", "w", encoding="utf-8") as file:
    file.write(content)
