# This program generates a random number between the lower and upper bounds
# entered by the user.

import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randint(lower_bound, upper_bound)

print(random_number)
