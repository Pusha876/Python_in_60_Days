# This program is to enumerate the list of filenames and capitalize
# the first letter of each filename

filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    row = f"{index}-{item.capitalize()}.txt"
    print(row)
