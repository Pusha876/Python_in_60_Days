countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for item in countries:
    file = open(f"{item}.txt", "w", encoding="utf-8")
    file.write(item)
    file.close()
