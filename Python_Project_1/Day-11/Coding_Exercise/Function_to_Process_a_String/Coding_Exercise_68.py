# The function should remove the last four characters from the string
# and return the result.

def format_filename():
    filename = "report.txt"
    file_name = filename[:-4].capitalize()
    return file_name


print(format_filename())
