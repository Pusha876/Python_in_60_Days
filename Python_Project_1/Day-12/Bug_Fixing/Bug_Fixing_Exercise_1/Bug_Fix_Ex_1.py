# this code is not working as expected. The function speed was calling the
# wrong parameters. The correct parameters are distance and time.
# The correct code is below.

def speed(distance, time):
    return distance / time


print(speed(200, 4))
