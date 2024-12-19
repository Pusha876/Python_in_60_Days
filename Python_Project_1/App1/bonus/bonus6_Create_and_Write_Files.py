contents = [
    "All my focus is now on the project",
    "I am working hard to complete it",
    "Currently on day 6 of the project"
]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w", encoding="utf-8")
    file.write(content)
    file.close()
