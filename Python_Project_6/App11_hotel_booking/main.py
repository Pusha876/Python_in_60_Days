import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str, "available": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing the availability status to no."""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available_rooms(self):
        """Check if the hotel is available for booking."""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = (
            f"Thank  you for your reservation! \n"
            f"Here are your booking information: \n"
            F"Name of the customer: {self.customer_name}, \n"
            f"Hotel name: {self.hotel.name}"
        )
        return content


print(df)
hotel_ID = input("Enter the id of the hotel you want to book: ")
hotel = Hotel(hotel_ID)
if hotel.available_rooms():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available.")
