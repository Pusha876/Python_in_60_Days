languages = ['English', 'German', 'Spanish']

for item in languages:
    with open(f"{item}.txt", "w", encoding="utf-8") as file:
        file.write(item)
