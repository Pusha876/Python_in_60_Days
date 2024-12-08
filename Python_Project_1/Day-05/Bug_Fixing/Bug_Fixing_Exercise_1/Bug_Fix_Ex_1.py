# This code now works as expected. The user can choose an item from the menu
# and the program will display the item that the user has chosen.

menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))

message = f"You have chosen {menu[user_choice]}."
print(message)
