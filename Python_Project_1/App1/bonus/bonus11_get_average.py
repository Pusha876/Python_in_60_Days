def get_average():
    with open("../files/data.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    average_value = sum(values) / len(values)
    return average_value


average = get_average()
print(average)
