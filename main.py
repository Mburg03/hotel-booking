import pandas as pd


class Hotel: 
    def __init__(self, id) -> None:
        self.id = id
        
    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel) -> None:
        self.customer_name = customer_name
        self.hotel = hotel
    
    def generate(self):
        content = f"Name of the customer, hotel name"
        return content


hotels_df = pd.read_csv("./hotels.csv")
print(hotels_df)

hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())

else:
    print("Hotel is not available.")
