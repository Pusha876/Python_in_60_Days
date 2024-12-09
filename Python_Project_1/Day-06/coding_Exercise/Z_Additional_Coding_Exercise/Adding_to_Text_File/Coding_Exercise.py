member = input("Enter the name of the member: ")

file = open("C:/Users/Jamie/Downloads/members.txt", "r", encoding="utf-8")
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("C:/Users/Jamie/Downloads/members.txt", "w", encoding="utf-8")
existing_members = file.writelines(existing_members)
file.close()
