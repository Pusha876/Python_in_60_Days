# This code needed an additional temperature line was added to the code
# to convert the numbers of the list to strings so they can be written
# to the text file

temperatures = [10, 12, 14]
temperatures = [str(i) + '\n' for i in temperatures]
file = open("file.txt", 'w', encoding='utf-8')

file.writelines(temperatures)
