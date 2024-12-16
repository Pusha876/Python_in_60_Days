# You are printing out the filenames without the extension.

filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for i in filenames:
    print(i[:-4])
