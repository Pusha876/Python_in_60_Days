# This function will return the maximum and minimum value
# from the list of grades.

def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    message = f"Max: {maximum}, Min: {minimum}"
    return message


print(get_max())
